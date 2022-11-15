Our study book/tutorial is https://www.postgresqltutorial.com/ along with other resources like W3C and the official Postgresql Documentation.


In the Postgresql tutorial, dvdrental is a test database that is provided for students to work through and learn.


Using docker, a student can the run code in the root of the project file (You can find the root of the project by navigating to where the `docker-compose.yml` file is located).

When you are the root of our project file, for sample data from the postgresql tutorial:

Deflate dvdrental.zip file:

`docker-compose exec postgres unzip sample-db/dvdrental.zip`

After deflating the dvdrental.zip, Create the database using Postgres' terminal commands:

`docker-compose exec postgres createdb dvdrental -U postgres`

After the database has been created, load the data as follows:

`docker-compose exec postgres pg_restore -U postgres -d dvdrental dvdrental.tar`

Some of the commands you find have been derived from the article this reference: https://www.postgresqltutorial.com/postgresql-getting-started/load-postgresql-sample-database/


## NOTE:

The student-workarea will be a place for students to submit in-class assignments as well as learn how to work with conflicts if any as well as using the `git pull` command among others.

When changes happen to the docker file, you might from time to time be required to rebuild containers, delete them or restart them if necessary. If you discover something that can improve our work flow, it is more than welcome to be added here.

When pushing code, remember to first create a branch and push your code, this is followed by creating a pull request.

When you are done working with a branch, remember to delete it.

