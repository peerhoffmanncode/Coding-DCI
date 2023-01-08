# - Talk about environments
# - Integration test (connecting things together)

# - Development
# - Test environments (rarely mocking db)
# - Production (after match - CLOUD!)

import psycopg2
import psycopg2.sql as sql
import os


def make_connection(database_name="flask_intro"):
    DATABASE_URL = os.environ.get("DATABASE_URL", None)
    if DATABASE_URL:
        # This is how we shall connect to the CI/CD and future production environments in the Cloud.
        connection = psycopg2.connect(DATABASE_URL)
    else:
        connection = psycopg2.connect(
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432",
            database=database_name,
        )
    connection.autocommit = True  # commit each entry to database automatically
    cur = connection.cursor()
    return dict(connection=connection, cur=cur)


class Reminder:
    cur = make_connection().get("cur")
    table_name = "reminders"

    def __init__(self, title, description) -> None:
        self.title = title
        self.id = None
        self.description = description

    def __repr__(self) -> str:
        return f"<Reminder id={self.id}, title='{self.title}', description='{self.description}'>"

    def save(self):
        """
        Stores the values of title and description in the table
        """
        try:
            self.cur.execute(
                f"""INSERT INTO {self.table_name} (title, description)
            VALUES('{self.title}', '{self.description}') RETURNING id, title, description"""
            )

            id, title, description = self.cur.fetchone()
            reminder_instance = Reminder(title, description)
            reminder_instance.id = id
            return reminder_instance
        except:
            raise Exception("Something terrible happened! Talk to the developer")

    @classmethod
    def find(cls, **kwargs):

        cls.cur.execute(
            f"SELECT column_name FROM information_schema.columns WHERE table_name='{cls.table_name}';"
        )
        available_columns = [column[0] for column in cls.cur.fetchall()]
        print(available_columns)
        query_details = ""
        for kwarg in kwargs:
            if kwarg in available_columns:

                # Sanatizing
                kwargs[kwarg] = (
                    str(kwargs[kwarg])
                    .replace(";", "")
                    .replace("--", "")
                    .replace("'", "")
                    .replace('"', "")
                )

                if len(query_details) > 0:
                    query_details += " AND "
                if kwarg == "id":
                    query_details += f"id={kwargs['id']}"
                else:
                    # alike preparing
                    new_s = " "
                    for c in str(kwargs[kwarg]):
                        if new_s[-1] != c:
                            new_s = new_s[0:] + c
                    kwargs[kwarg] = "%".join(list(new_s)).strip()

                if kwarg == "title":
                    query_details += f"title LIKE '{kwargs['title']}%'"
                if kwarg == "description":
                    query_details += f"description LIKE '{kwargs['description']}%'"
        try:
            cls.cur.execute(
                f"SELECT id, title, description FROM {cls.table_name} WHERE {query_details};"
            )

            id, title, description = cls.cur.fetchone()

            reminder_instance = cls(title=title, description=description)
            reminder_instance.id = id
            return reminder_instance
        except Exception as e:
            print(e)
            return None

    # TODO: Inclass
    @classmethod
    def all(cls):
        # return all reminders
        cls.cur.execute(f"SELECT id, title, description FROM {cls.table_name};")
        reminders = cls.cur.fetchall()

        reminder_list = []
        for r in reminders:
            # create an instance
            reminder_instance = cls(title=r[1], description=r[2])
            reminder_instance.id = r[0]
            # add the instance to the list
            reminder_list.append(reminder_instance)
        return reminder_list

    @classmethod
    def delete(cls, id):
        try:
            cls.cur.execute(f"DELETE FROM {cls.table_name} WHERE id = {id};")
            return f"{id} was deleted successfully", 204
        except:
            return "Something went wrong!", 500
