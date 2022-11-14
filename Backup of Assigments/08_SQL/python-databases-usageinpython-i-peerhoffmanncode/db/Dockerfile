# base image
FROM postgres:11-alpine

# run create.sql on init
ADD create.sql /docker-entrypoint-initdb.d

# Using the data from https://www.postgresqltutorial.com/postgresql-getting-started/load-postgresql-sample-database/
# ADD dvdrental.zip /sample-db/dvdrental.zip
