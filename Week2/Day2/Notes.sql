

--SQL DAAYYYY (and mySQL)

CREATE TABLE countries	(
	country_id integer PRIMARY key
	,country text UNIQUE NOT NULL
	,population integer
	,area real
);

INSERT INTO countries	(
	(country, population, area)
)

VALUES
	('Austria', 8700000, 84000)
	('Switzerland', 8400000, 41000)
	('Germany', 82000000, 360000)
	('Liechtenstein', 57000, 160)
;

SELECT * 
FROM countries;

DELETE FROM countries;

UPDATE countries
SET area = 160
WHERE country = 'Liechtenstein'

SELECT 
	cus.customerid,
	cus.customername,
	prd.customerid
FROM customers cts
INNER JOIN products prd.productid
GROUP BY 
	cus.customerid,
	cus.customername
ON ord.orderid
ORDER BY total_spent DESC


