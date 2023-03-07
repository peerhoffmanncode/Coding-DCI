# Reminder application

The `Reminder application` makes it easier than ever to remember the things you need to do.
You can use it for all of life's to-dos including grocery lists, projects at work and anything else you want to track.

# How to run this application

You have two ways to run the application, the better way will be to run it via docker.

Build the entire application like this:

`docker-compose up -d --build`

The frontend application is running in the following page:

- [http://localhost:8080/](http://localhost:8080)

The backend application can be accessed using the following URL:

- [http://localhost:5050/](http://localhost:5050)


The second way to run this application is individually.

Navigate to each of the folders and follow the instructions in the respective README files.

## Start the application after build step

`docker-compose up -d`

This will enable 3 micro-services we need for our application

- database service (postgresql)
- redis service (a good tech for caching and speeding things up in backend systems)
- actual application code (api service)

## Accessing the database


`docker-compose exec postgres psql -U postgres`

Please note that the part after `exec` depends on how the developer labels the service in the `docker-compose.yml` file.

The syntax for such commands will look like this:

`docker-compose exec <service name> <command>`

## Accessing redis

`docker-compose exec redis redis-cli`


## Accessing the API's bash (You get to see code in the container)

`docker-compose exec api bash`
