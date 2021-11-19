-- show average temperatures for cities
SELECT city, avg(value) FROM temperatures GROUP BY city ORDER BY avg(value) DESC;