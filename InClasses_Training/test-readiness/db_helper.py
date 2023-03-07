import psycopg2


def db_get_connect(db_name):
    """create a connection to psycopg and return object"""
    db_connection = psycopg2.connect(f"dbname={db_name} user=postgres")
    return db_connection


def db_close_connect(db_connection) -> None:
    """close connection to psycopg"""
    db_connection.close()


def db_write(db_connection, query: str) -> None:
    """write a query to database"""
    db_cursor = db_connection.cursor()
    db_cursor.execute(query)
    db_cursor.close()
    db_connection.commit()


def db_read(db_connection, query: str, mode: str = "") -> list:
    """read from database"""
    db_cursor = db_connection.cursor()
    db_cursor.execute(query)
    if mode == "all":
        db_response = db_cursor.fetchall()
    else:
        db_response = db_cursor.fetchone()
    db_cursor.close()
    return db_response
