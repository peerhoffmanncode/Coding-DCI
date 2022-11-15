---Select limit and concantenation of colums , as
SELECT * FROM actor;
SELECT * FROM customer;
SELECT first_name FROM customer;

SELECT  first_name, last_name, email FROM customer;
SELECT first_name || ' ' || last_name, email FROM customer;

---Alias -- as 
SELECT  email as e_mail , first_name, last_name FROM  customer  LIMIT  10  ;
SELECT  email   e_mail ,  first_name, last_name FROM  customer  LIMIT  10  ;

SELECT  email as e_mail , first_name as inials , last_name as family_name  FROM  customer  LIMIT  10  ;
SELECT  email  e_mail , first_name  inials , last_name  family_name  FROM  customer  LIMIT  10  ;
SELECT first_name || ' ' || last_name as full_mame, email FROM customer;
SELECT first_name || ' ' || last_name as "full name", email FROM customer;

---ORDER BY--- 

SELECT first_name, last_name FROM customer ORDER BY first_name ASC;
SELECT first_name, last_name FROM customer ORDER BY last_name  ASC;
SELECT first_name, last_name FROM customer ORDER BY last_name  ASC , first_name DESC ;

---concatenation
SELECT first_name || ' '  || last_name   as "full name ",  last_update   FROM customer ORDER BY last_update   ASC;


SELECT  first_name, LENGTH(first_name) len FROM customer ORDER BY  len DESC;

SELECT  first_name, LENGTH(first_name) len_name  FROM customer ORDER BY  len_name  DESC;
SELECT  first_name, LENGTH(first_name) len_name  FROM customer ORDER BY  len_name  ASC;

-- create a new table
CREATE TABLE sort_demo(num INT);

-- insert some data
INSERT INTO sort_demo(num) VALUES (1),(2),(3),(null);

SELECT  num from sort_demo  order by num;
SELECT  num from sort_demo  order by  num NULLS LAST;
SELECT  num from sort_demo  order by  num NULLS FIRST;

---null first
SELECT  num from sort_demo  order by  num DESC;
---null last forced
SELECT  num from sort_demo  order by  num DESC nulls last;
