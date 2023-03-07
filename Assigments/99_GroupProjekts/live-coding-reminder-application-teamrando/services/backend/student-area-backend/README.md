The instructions below are to be used via the docker interface:


# Copy file

Make a copy of the file you find in `victor/usage_in_python.py` and put it in your own folder
e.g. 

`student-area-backend/<your name>`

# Create a database

Create a database called `python_practice`

In the root of your project do the following:

`docker-compose exec postgres createdb python_practice -U postgres`

_You can also create the database using DBeaver alternatively._

# Update the Python script with commands like CREATE, INSERT and maybe SELECT

`docker-compose exec api python student-area-backend/<your name>/name-of-your-script.py`