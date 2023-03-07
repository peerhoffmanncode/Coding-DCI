\d actor
SELECT first_name FROM actor;
SELECT * FROM actor;
SELECT first_name, last_name FROM actor;
SELECT first_name || ' ' || last_name, actor_id FROM actor;
SELECT 5*7;


SELECT first_name AS fn FROM actor;
SELECT last_name ln FROM actor;
SELECT first_name ||' '|| last_name full_name FROM actor;
SELECT first_name ||' '|| last_name "full name" FROM actor;

SELECT first_name, last_name FROM actor ORDER BY last_name ASC;
SELECT first_name ||' '|| last_name "full name" FROM actor ORDER BY last_name ASC;
SELECT first_name ||' '|| last_name "full name" FROM actor ORDER BY last_name DESC;
SELECT first_name, LENGTH(first_name) len FROM actor ORDER BY len DESC;
SELECT num FROM sort_demo ORDER BY num;
SELECT num FROM sort_demo ORDER BY num NULLS FIRST;
SELECT num FROM sort_demo ORDER BY num DESC;