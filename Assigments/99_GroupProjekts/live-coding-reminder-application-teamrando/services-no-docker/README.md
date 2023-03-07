# Reminder application

The `Reminder application` makes it easier than ever to remember the things you need to do.
You can use it for all of life's to-dos including grocery lists, projects at work and anything else you want to track.

# How to run this application

In the current folder, go into the frontend project and then run the command below:

`cd frontend`

Start the frontend server:

`python3 -m http.server 8080`

The frontend application is running in the following page:

- [http://localhost:8080/](http://localhost:8080)

# How to handle the database

Create the database we shall use for the reminders application (ou have to be in the `db` folder):

`psql < create.sql -U postgres`

## Accessing the database

`psql -U postgres`

To see the list of databases check this out:

- List databases: `\l`
- Connecting to the database: `\c <name of database>`

Commands like `SELECT`, `INSERT` can be used in the PSQL prompt as well as in Python.

## Running the Flask project

The flask project can be found in the `backend` folder. 

The first step is to make sure there is a virtual environment:

Be in the correct folder in the terminal:

`cd backend`

Create a virtual environment

`python3 -m venv venv`

Activate the virtual environment

`source venv/bin/activate`

Install the dependences that have been provided in the `requirements.txt` file

`pip install -r requirements.txt`

Run the flask project as follows after:

`python app.py`

... another command that works is:

`FLASK_DEBUG=true flask run`

The backend application can be accessed using the following URL:

- [http://localhost:5050/](http://localhost:5050)
