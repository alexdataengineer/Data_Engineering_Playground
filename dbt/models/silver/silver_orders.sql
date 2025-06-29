{{
    config(
        materialized='incremental',
        partition_by={
            "field": "order_date",
            "data_type": "date",
            "granularity": "day"
        },
        cluster_by=['user_id'],
        tags=['silver', 'orders'],
        unique_key=['order_id']
    )
}}


WITH source_data AS (
    SELECT 
        id,
        created_at,
        user_id,
        product_id,
        quantity,
        unit_price,
        
        COALESCE(updated_at, created_at) as last_modified_at
    FROM {{ ref('bronze_orders') }}
    WHERE created_at IS NOT NULL  
    {% if is_incremental() %}
        AND COALESCE(updated_at, created_at) > (SELECT max(last_modified_at) FROM {{ this }})
    {% endif %}
),

transformed_data AS (
    SELECT
        MD5(CONCAT(CAST(id AS STRING), CAST(created_at AS STRING))) as order_id,
        id as original_order_id,
        CAST(date_format(created_at, 'yyyy-MM-dd') AS DATE) as order_date,
        CAST(user_id AS STRING) as user_id,
        CAST(product_id AS STRING) as product_id,
        CAST(quantity AS INTEGER) as quantity,
        CAST(unit_price AS DECIMAL(10,2)) as unit_price,
        CAST(quantity * unit_price AS DECIMAL(10,2)) as order_amount,
        CASE 
            WHEN quantity * unit_price >= 1000 THEN 'High Value'
            WHEN quantity * unit_price >= 500 THEN 'Medium Value'
            ELSE 'Standard Value'
        END as order_value_category,
        CURRENT_TIMESTAMP() as _loaded_at,
        '{{ invocation_id }}' as _run_id,
        COALESCE(updated_at, created_at) as last_modified_at
    FROM source_data
)

SELECT * FROM transformed_data
WHERE quantity > 0  -- Business rule: orders must have positive quantity
  AND unit_price > 0  -- Business rule: unit price must be positive
  AND order_amount <= 1000000  -- Business rule: maximum order amount
  AND LENGTH(TRIM(user_id)) > 0  -- Business rule: user_id cannot be empty
  AND LENGTH(TRIM(product_id)) > 0  -- Business rule: product_id cannot be empty