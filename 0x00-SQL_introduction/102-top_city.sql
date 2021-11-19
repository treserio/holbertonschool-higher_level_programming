-- show top 3 city's with highest avg temp for months 7 & 8
SELECT city, AVG(value) AS avg_temp FROM temperatures
    WHERE month = 7 OR month = 8
    GROUP BY city
    ORDER BY AVG(value)
    DESC LIMIT 3;
