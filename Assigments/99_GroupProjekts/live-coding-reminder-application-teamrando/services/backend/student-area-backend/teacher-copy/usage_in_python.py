import psycopg2
# Documentation: https://www.psycopg.org/docs/

connection = psycopg2.connect(
    user='postgres', 
    password='postgres', 
    host='postgres', 
    port='5432', 
    database='python_practice'
)

curr = connection.cursor()
curr.execute("CREATE TABLE casino(id SERIAL PRIMARY KEY, name VARCHAR(255))")
connection.commit()
connection.close()

print("Postgres SQL commands executed successfully!")