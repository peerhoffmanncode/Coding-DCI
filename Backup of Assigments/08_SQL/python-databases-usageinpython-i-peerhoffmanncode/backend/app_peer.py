import psycopg2
import datetime

# Database init SQL query script
# drop any existing table to start from scratch
# create tables as requested
# insert data as requested
INIT_SCRIPT = [
    "DROP TABLE IF EXISTS warehouse, employee",
    "CREATE TABLE warehouse \
        (id serial NOT NULL PRIMARY KEY, warehouse_name VARCHAR (100) NOT NULL, \
            employee_count serial);"
    "INSERT INTO warehouse \
        (id, warehouse_name, employee_count) \
        VALUES ('1', 'Amazon Warehouse', 1000), ('2', 'Rewe Warehouse', 400), \
            ('3', 'Tedi Warehouse', 200), ('4', 'Bahn Warehouse', 1500);"
    "CREATE TABLE employee \
        (id serial NOT NULL PRIMARY KEY, employee_name VARCHAR (100) NOT NULL, \
            warehouse_id serial NOT NULL, joining_date DATE NOT NULL, \
                speciality VARCHAR (100) NOT NULL, salary INTEGER NOT NULL, \
                experience SMALLINT);"
    "INSERT INTO employee \
        (id, employee_name, warehouse_id, joining_date, speciality, salary, experience) \
            VALUES ('101', 'Mo', '1', '2005-2-10', 'HR Manager', '40000', NULL),\
            ('102', 'Michael', '1', '2018-07-23', 'Driver', '30000', NULL),\
            ('103', 'Lukaku', '2', '2016-05-19', 'Conveyor', '25000', NULL),\
            ('104', 'Robert', '2', '2017-12-28', 'Logistics Spcialist', '28000', NULL),\
            ('105', 'Linda', '3', '2004-06-04', 'Logistics Spcialist', '42000', NULL),\
            ('106', 'Kahn', '3', '2012-09-11', 'Manager', '30000', NULL),\
            ('107', 'Bernice', '4', '2014-08-21', 'Medic', '32000', NULL),\
            ('108', 'Karen', '4', '2011-10-17', 'Driver', '30000', NULL);",
]


# Postgres cention constants
USER = "postgres"
PASSWORD = "postgres"
HOST = "postgres"
PORT = "5433"
DB = "warehouse_db"


def write_to_database(execution_script=None) -> None:
    """function to write data into a database"""
    if not execution_script:
        return

    # open the database
    connection = psycopg2.connect(
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT,
        database=DB,
    )
    curr = connection.cursor()
    # execute a sql script
    for script_line in execution_script:
        curr.execute(script_line)
    # commit the changes to the database
    connection.commit()
    # close the database
    connection.close()


def read_from_database(execution_script=None) -> list:
    """function to read from a database"""
    if not execution_script:
        return [""]

    # open the database
    connection = psycopg2.connect(
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=POST,
        database=DB,
    )
    curr = connection.cursor()
    # execute a sql script
    for script_line in execution_script:
        curr.execute(script_line)
    db_content = curr.fetchall()
    # commit the changes to the database
    connection.commit()
    # close the database
    connection.close()
    return db_content


def get_warehouse_detail(warehouse_id) -> tuple:
    """function to get the details of a warehouse"""
    query = [
        f"SELECT id, warehouse_name, employee_count FROM warehouse WHERE id={warehouse_id}"
    ]
    return read_from_database(query)[0]


def read_database_version():
    """function to get the details of a database version"""
    return read_from_database(["SELECT version();"])[0][0]


def get_employee_detail(employee_id) -> tuple:
    """function to get the details of a employee"""
    query = [
        f"SELECT id, employee_name, warehouse_id, joining_date, \
            speciality, salary, experience FROM employee WHERE id={employee_id}"
    ]
    return read_from_database(query)[0]


def update_employee_experience(employee_id) -> tuple:
    """function to update employees experience"""
    # create query to find employee joining_date
    emp_joining_date = f"(SELECT joining_date FROM employee WHERE id={employee_id})"
    # create query to calculate date_diff_query -> embedding emp_joining_date query!
    date_diff_query = f"DATE_PART('year', '{datetime.date.today()}'::date) - DATE_PART('year', {emp_joining_date}::date)"
    # create query to update_query employee experience, embedding date_diff_query!
    update_query = [
        f"UPDATE employee SET experience = ({date_diff_query}) WHERE id={employee_id};"
    ]
    # update SQL database - yeah, my first structure :-) !
    write_to_database(update_query)

    # return update
    gather_query = [
        f"SELECT id, employee_name, warehouse_id, joining_date, speciality, \
            salary, experience FROM employee WHERE id={employee_id}"
    ]
    return read_from_database(gather_query)[0]


def update_employee_experience_python_math(employee_id) -> tuple:
    """function to update employees experience"""

    gather_query = [
        f"SELECT id, employee_name, warehouse_id, joining_date, speciality, \
            salary, experience FROM employee WHERE id={employee_id}"
    ]
    # read 3rd element (join date) from the return,
    # get the year of the string and convert to integer
    employee_joining_date = int(read_from_database(gather_query)[0][3].strftime("%Y"))

    # crazy math here!
    new_employee_experience = (
        int(datetime.datetime.now().strftime("%Y")) - employee_joining_date
    )

    # update database
    update_query = [
        f"UPDATE employee SET experience={new_employee_experience} WHERE id={employee_id}"
    ]
    write_to_database(update_query)

    # return update
    return read_from_database(gather_query)[0]


def get_specialist_employee_list(speciality, salary) -> list:
    """function to get special employee's"""
    query = [
        f"SELECT id, employee_name, warehouse_id, joining_date, speciality, \
            salary, experience FROM employee WHERE speciality='{speciality}' \
            AND salary>{salary-1}"
    ]
    return read_from_database(query)


def create_employee(empolyee_sql_query):
    """function to create new employee in database as per the SQL query
    passed to the function."""

    # open db and write
    write_to_database([empolyee_sql_query])


def main():
    # init database
    write_to_database(INIT_SCRIPT)

    # get postgres version
    print(f"Postgres Version: {read_database_version()}")
    print()
    print()

    print("Question 2: Read given warehouse and employee details")
    print("Printing Warehouse record")
    db_readout = get_warehouse_detail(2)
    print(f"Warehouse Id: {db_readout[0]}")
    print(f"Warehouse Name: {db_readout[1]}")
    print(f"Employee Count: {db_readout[2]}")
    print()
    print("Printing Employee record")
    db_readout = get_employee_detail(105)
    print(f"Employee Id: {db_readout[0]}")
    print(f"Employee Name: {db_readout[1]}")
    print(f"Warehouse Id: {db_readout[2]}")
    print(f"Joining Date: {db_readout[3]}")
    print(f"Specialty: {db_readout[4]}")
    print(f"Salary: {db_readout[5]}")
    print(f"Experience: {db_readout[6]}")
    print()
    print()

    print("Question 3: Update Employee experience in years")
    print("Printing Employee record")
    print()
    print("== BEFORE database update ==")
    db_readout = get_employee_detail(101)
    print(f"Employee Id: {db_readout[0]}")
    print(f"Employee Name: {db_readout[1]}")
    print(f"Warehouse Id: {db_readout[2]}")
    print(f"Joining Date: {db_readout[3]}")
    print(f"Specialty: {db_readout[4]}")
    print(f"Salary: {db_readout[5]}")
    print(f"Experience: {db_readout[6]}")
    print()
    print("== AFTER database update ==")
    db_readout = update_employee_experience(101)
    print(f"Employee Id: {db_readout[0]}")
    print(f"Employee Name: {db_readout[1]}")
    print(f"Warehouse Id: {db_readout[2]}")
    print(f"Joining Date: {db_readout[3]}")
    print(f"Specialty: {db_readout[4]}")
    print(f"Salary: {db_readout[5]}")
    print(f"Experience: {db_readout[6]}")
    print()
    print()

    print("Question 4: Get the list Of employees as per specialty and salary")
    print("Printing employees whose specialty is Driver and salary greater than 30000")
    db_readout = get_specialist_employee_list("Driver", 30_000)
    for employee_found in db_readout:
        print(f"Employee Id: {employee_found[0]}")
        print(f"Employee Name: {employee_found[1]}")
        print(f"Warehouse Id: {employee_found[2]}")
        print(f"Joining Date: {employee_found[3]}")
        print(f"Specialty: {employee_found[4]}")
        print(f"Salary: {employee_found[5]}")
        print(f"Experience: {employee_found[6]}")
        print()
    print()

    print("Question 5: Insert a record for a new Employee")
    print("Inserting employee into database")
    create_employee(
        "INSERT INTO employee (id, employee_name, warehouse_id, joining_date, \
            speciality, salary, experience) \
            VALUES ('109', 'Olivia', '2', '2021-09-10', 'Consultant', '67500', NULL)"
    )
    print()
    db_readout = get_employee_detail(109)
    print(f"Employee Id: {db_readout[0]}")
    print(f"Employee Name: {db_readout[1]}")
    print(f"Warehouse Id: {db_readout[2]}")
    print(f"Joining Date: {db_readout[3]}")
    print(f"Specialty: {db_readout[4]}")
    print(f"Salary: {db_readout[5]}")
    print(f"Experience: {db_readout[6]}")
    print()


if __name__ == "__main__":
    main()
    # confirm that the database has changed
    print("successfully interacted with database!")
