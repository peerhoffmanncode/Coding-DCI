-- SELECT statement, FROM and AS clauses.
SELECT first_name FROM customer;
SELECT first_name, last_name FROM customer;
SELECT first_name, last_name, email FROM customer;
SELECT * FROM customer;
SELECT first_name || ' ' || last_name, email FROM customer;

/*purpose of AS is to assign temporary names to columns in queries.
Use double quotes (“) to surround a column alias that contains spaces.*/
SELECT first_name AS "Name", last_name AS "Surname" FROM customer;
SELECT first_name || ' ' || last_name AS "Full name", email FROM customer;

--ORDER BY clause.
--ascending order is the default.
SELECT first_name, last_name FROM customer ORDER BY  first_name ASC;
--descending order. 
SELECT first_name, last_name FROM customer ORDER BY  first_name DESC; 
--ORDER BY clause can be used with multiple columns.
SELECT first_name, last_name 
FROM customer  
ORDER BY first_name ASC, last_name DESC;

--The LENGTH() function accepts a string and returns the length of that string.
SELECT first_name AS "Name", LENGTH(first_name) AS "Length of Name" 
FROM customer
ORDER BY LENGTH(first_name) DESC;
--NULL is a marker that indicates the missing data or the data is unknown. 
SELECT last_update from film ORDER BY last_update  NULLS LAST;

-- to run sql file in psql use \i path_ to_file.sql
/* \i live-coding-reminder-application-teamrando/services/student-workarea/Muhannad/dvdrental.sql */
