/* Simnple selection */

SELECT * FROM actor;
SELECT first_name FROM actor;
SELECT first_name, last_name FROM actor;
SELECT actor_id, first_name, last_name FROM actor;

/* Selection using concatination */
SELECT
    first_name || ' ' || last_name,
    email
FROM
    customer;

/* Using aliases for colomns */
SELECT first_name AS fn FROM actor;
SELECT first_name, last_name AS surname FROM customer;
/* Using aliases for c */
SELECT
    first_name || ' ' || last_name AS full_name
FROM
    customer;
/* Using aliases - spaced aliases need to be surrounded by quotes */
SELECT
    first_name || ' ' || last_name "full name"
FROM
    customer;


/* Using ordered by ascending or descending */
SELECT
	first_name,
	last_name
FROM
	actor
ORDER BY
	first_name ASC;

/* using different ordering [ASC/DSC] */
SELECT
	first_name,
	last_name
FROM
	actor
ORDER BY
	first_name ASC,
	last_name DESC;

/* using different functions LENGTH >var to store to< as well as ORDER ... */
/* found out about the importance of Lollobrigida ... well ! */
SELECT
	first_name,
	LENGTH(first_name) len_fn,
    last_name,
    LENGTH(last_name) len_ln
FROM
	actor
ORDER BY
	len_ln DESC;

/* handling the NULL marker in the db */
SELECT
	first_name,
	LENGTH(first_name) len_fn
FROM
	actor
ORDER BY
    first_name NULLS FIRST;

/* Using WHERE */
SELECT
	first_name,
    last_name,
    LENGTH(first_name) len_fn,
    LENGTH(last_name) len_ln
FROM
	actor
WHERE
    first_name='Kevin';
