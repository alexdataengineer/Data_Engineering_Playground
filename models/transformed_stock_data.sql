{{ config(materialized='view') }}  -- Define que esse modelo será uma VIEW

WITH stock_data AS (
    SELECT
        Date,
        [Open],
        High,
        Low,
        [Close],
        Volume,
        ([Close] - [Open]) AS daily_change,
        ([Close] - [Open]) / [Open] * 100 AS daily_change_pct,
        High - Low AS daily_range,
        AVG([Close]) OVER (ORDER BY Date ROWS BETWEEN 9 PRECEDING AND CURRENT ROW) AS moving_avg_10,
        SUM(Volume) OVER (ORDER BY Date ROWS BETWEEN 9 PRECEDING AND CURRENT ROW) AS rolling_volume
    FROM {{ source('dbo', 'stock_data') }}
)

SELECT * FROM stock_data;

