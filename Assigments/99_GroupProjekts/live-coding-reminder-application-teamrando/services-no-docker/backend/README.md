# Backend API

This is a project that will power the frontend project of a reminders application.

At its current stage there is not much that works. Install dependencies:

Steps to setup project

- Create a virtual environment
- Activate the virtual environment and then install dependencies:

    `pip install -r requirements.txt`

- Create a database, see the SQL script that we can use at the root of the project `./services/db/create.sql`


Run it in development mode as follows:

`FLASK_DEBUG=true flask run`

Possible issues:

Connecting to postgresql you may have to work with system environment variables and access them through the `os` module.
