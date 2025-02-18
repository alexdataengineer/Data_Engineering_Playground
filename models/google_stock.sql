WITH source_data AS (
    SELECT TOP 10000  
        CAST(date AS DATE) AS trade_date,
        CAST(adj_close AS DECIMAL(18,4)) AS adjusted_close_price,
        CAST([close] AS DECIMAL(18,4)) AS closing_price,  
        CAST(high AS DECIMAL(18,4)) AS highest_price,
        CAST(low AS DECIMAL(18,4)) AS lowest_price,
        CAST([open] AS DECIMAL(18,4)) AS opening_price,  
        CAST(volume AS BIGINT) AS trade_volume
    FROM {{ source('dbo', 'googl_data_2020_2025_cleaned') }}
)
SELECT * FROM source_data;

