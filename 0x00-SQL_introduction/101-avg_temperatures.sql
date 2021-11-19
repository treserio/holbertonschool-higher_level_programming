-- show average temperatures for cities
SELECT city, avg(value) AS agv_temp FROM temperatures GROUP BY city ORDER BY avg(value) DESC;