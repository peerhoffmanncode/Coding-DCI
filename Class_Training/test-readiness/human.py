from db_helper import db_get_connect, db_close_connect, db_read, db_write
import psycopg2
import os


def connect_db():
    uri = os.environ.get(
        "DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/tdd_test"
    )
    connection = psycopg2.connect(uri)
    cur = connection.cursor()
    return connection, cur


db_con, db_cur = connect_db()


class Human:
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def save(self):
        # db_write
        print(db_read(db_con, "SELECT * FROM pokemons;", "all"))
