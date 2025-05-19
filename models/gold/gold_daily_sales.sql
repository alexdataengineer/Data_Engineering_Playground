{{
    config(
        schema = 'gold'
    )
}}

SELECT
  o.order_date,
  p.product_name,
  p.category,
  p.vendor,
  u.city,
  u.state,
  u.sales_channel,
  SUM(o.order_amount) AS total_revenue
FROM 
  {{ ref('silver_orders') }} o
LEFT JOIN {{ ref('silver_products') }} p
  ON o.product_id = p.id
LEFT JOIN {{ ref('silver_users') }} u
  ON o.user_id = u.id
GROUP BY
  o.order_date,
  p.product_name,
  p.category,
  p.vendor,
  u.city,
  u.state,
  u.sales_channel
