-- show average temperatures for cities
SELECT city, AVG(value) AS agv_temp FROM temperatures GROUP BY city ORDER BY AVG(value) DESC;
