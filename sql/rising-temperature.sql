SELECT id
FROM (
    SELECT 
        id, 
        temperature,
        recordDate,
        LAG(temperature) OVER (ORDER BY recordDate) AS prev_temp,
        LAG(recordDate) OVER (ORDER BY recordDate) AS prev_date
    FROM Weather
) AS temp_with_prev
WHERE temperature > prev_temp AND DATEDIFF(recordDate, prev_date) = 1;
