{{
    config(
        materialized='incremental',
        tags=['bronze', 'orders'],
        unique_key=['id']
    )
}}

/*
    Bronze layer for orders data.
    This model:
    - Performs initial data validation
    - Applies basic type casting
    - Handles incremental processing
    - Adds metadata columns
*/

WITH source_data AS (
    SELECT 
        id,
        created_at,
        updated_at,
        user_id,
        product_id,
        quantity,
        unit_price,
        payment_type,
        payment_sequential,
        payment_installments,
        order_status,
        order_purchase_date,
        order_approved_date,
        order_delivered_carrier_date,
        order_delivered_customer_date,
        freight_value
    FROM {{ source('default', 'orders') }}
    {% if is_incremental() %}
        WHERE COALESCE(updated_at, created_at) > (SELECT max(COALESCE(updated_at, created_at)) FROM {{ this }})
    {% endif %}
),

validated_data AS (
    SELECT
        -- Primary key and identifiers
        CAST(id AS STRING) as id,
        CAST(user_id AS STRING) as user_id,
        CAST(product_id AS STRING) as product_id,
        
        -- Timestamps
        CAST(created_at AS TIMESTAMP) as created_at,
        CAST(updated_at AS TIMESTAMP) as updated_at,
        CAST(order_purchase_date AS TIMESTAMP) as order_purchase_date,
        CAST(order_approved_date AS TIMESTAMP) as order_approved_date,
        CAST(order_delivered_carrier_date AS TIMESTAMP) as order_delivered_carrier_date,
        CAST(order_delivered_customer_date AS TIMESTAMP) as order_delivered_customer_date,
        
        -- Numeric fields
        CAST(quantity AS INTEGER) as quantity,
        CAST(unit_price AS DECIMAL(10,2)) as unit_price,
        CAST(freight_value AS DECIMAL(10,2)) as freight_value,
        CAST(payment_sequential AS INTEGER) as payment_sequential,
        CAST(payment_installments AS INTEGER) as payment_installments,
        
        -- String fields
        CAST(payment_type AS STRING) as payment_type,
        CAST(order_status AS STRING) as order_status,
        
        -- Metadata
        CURRENT_TIMESTAMP() as _loaded_at,
        '{{ invocation_id }}' as _run_id
    FROM source_data
    WHERE id IS NOT NULL  -- Ensure primary key is not null
      AND user_id IS NOT NULL  -- Ensure required fields are not null
      AND product_id IS NOT NULL
      AND quantity > 0  -- Basic business rule validation
      AND unit_price > 0
)

SELECT * FROM validated_data

