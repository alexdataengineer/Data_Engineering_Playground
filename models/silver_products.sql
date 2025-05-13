SELECT 
id,
created_at,
title as product_name,
category,
ean,
vendor,
price
FROM 
{{ ref('bronze_product') }}