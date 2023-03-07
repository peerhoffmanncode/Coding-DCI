import psycopg2

# You have to create a database called `python_practice`
# in the root, you can do the following
# docker-compose exec postgres createdb python_practice -U postgres

# "CREATE TABLE IF NOT EXISTS casino(id SERIAL PRIMARY KEY, name VARCHAR(255))"

# Design of a SQL script
SCRIPT = [
    "INSERT INTO casino (name) VALUES ('Emily')",
    "INSERT INTO casino (name) VALUES ('Michel')",
    "INSERT INTO casino (name) VALUES ('Fausto')",
    "INSERT INTO casino (name) VALUES ('Waheed')",
    "INSERT INTO casino (name) VALUES ('Nadia')",
    "INSERT INTO casino (name) VALUES ('Somon')",
    "CREATE TABLE IF NOT EXISTS registration(id SERIAL PRIMARY KEY, name VARCHAR(255), registration_date DATE)",
]
# open the database
connection = psycopg2.connect(
    user="postgres",
    password="postgres",
    host="postgres",
    port="5432",
    database="python_practice",
)
curr = connection.cursor()
# execute a sql script
for script_line in SCRIPT:
    curr.execute(script_line)
# commit the changes to the database
connection.commit()
# close the database
connection.close()

# confirm that the database has changed
print("successfully changed database!")
