SELECT 
id,
date_format(created_at, 'yyyy-MM-dd') as order_date,
user_id,
product_id,
quantity,
unit_price,
quantity * unit_price as order_amount
FROM {{ ref('bronze_orders') }}