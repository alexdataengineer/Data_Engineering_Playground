{{
    config(
        materialized='incremental',
        tags=['bronze', 'orders'],
        unique_key=['id'],
        indexes=[
            {'columns': ['user_id']},
            {'columns': ['product_id']},
            {'columns': ['order_purchase_date']}
        ]
    )
}}


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
        
        -- Calculated fields
        CAST(quantity * unit_price AS DECIMAL(10,2)) as total_amount,
        CAST(quantity * unit_price + freight_value AS DECIMAL(10,2)) as total_amount_with_freight,
        
        -- Order metrics
        CASE 
            WHEN order_status = 'delivered' AND order_delivered_customer_date IS NOT NULL 
            THEN DATEDIFF(day, order_purchase_date, order_delivered_customer_date)
            ELSE NULL 
        END as delivery_time_days,
        
        CASE 
            WHEN order_status = 'delivered' AND order_delivered_carrier_date IS NOT NULL 
            THEN DATEDIFF(day, order_purchase_date, order_delivered_carrier_date)
            ELSE NULL 
        END as carrier_delivery_time_days,
        
        -- Payment metrics
        CASE 
            WHEN payment_installments > 1 THEN 'installment'
            ELSE 'single_payment'
        END as payment_method_type,
        
        -- Status tracking
        CASE 
            WHEN order_status = 'delivered' AND order_delivered_customer_date IS NOT NULL THEN 'completed'
            WHEN order_status = 'shipped' THEN 'in_transit'
            WHEN order_status = 'processing' THEN 'processing'
            ELSE 'pending'
        END as order_status_category,
        
        -- Metadata
        CURRENT_TIMESTAMP() as _loaded_at,
        '{{ invocation_id }}' as _run_id,
        '{{ env_var("DBT_CLOUD_RUN_ID", "manual") }}' as _dbt_run_id
    FROM source_data
    WHERE id IS NOT NULL  -- Ensure primary key is not null
      AND user_id IS NOT NULL  -- Ensure required fields are not null
      AND product_id IS NOT NULL
      AND quantity > 0  -- Basic business rule validation
      AND unit_price > 0
      AND order_purchase_date IS NOT NULL  -- Required timestamp
      AND order_status IS NOT NULL  -- Required status
      AND payment_type IS NOT NULL  -- Required payment info
      AND LENGTH(TRIM(id)) > 0  -- Ensure no empty strings
      AND LENGTH(TRIM(user_id)) > 0
      AND LENGTH(TRIM(product_id)) > 0
      AND LENGTH(TRIM(order_status)) > 0
      AND LENGTH(TRIM(payment_type)) > 0
)

SELECT * FROM validated_data

