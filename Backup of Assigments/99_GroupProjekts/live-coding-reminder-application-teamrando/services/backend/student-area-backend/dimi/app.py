import psycopg2

# You have to create a database called `python_practice`
# in the root, you can do the following
# docker-compose exec postgres createdb python_practice -U postgres

connection = psycopg2.connect(
    user='postgres', 
    password='postgres', 
    host='postgres', 
    port='5432', 
    database='postgres'
)
curr = connection.cursor()
curr.execute("CREATE TABLE aek(first_name VARCHAR(50), date_of_registration DATE, id INT)")

for i in range(251):
    curr.execute(f"INSERT INTO aek(first_name, date_of_registration, id)VALUES ('baladoros', '2022-11-11', {i})")

connection.commit()
connection.close()
print("Finally")