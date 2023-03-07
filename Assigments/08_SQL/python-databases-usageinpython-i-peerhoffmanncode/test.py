import unittest
import datetime
import time

# Wait till all other docker container are executed!
# if app_peer.py wasn't executed, the database is not prepared with data
time.sleep(7)

# import functions from solutions
from app.app_peer import read_database_version
from app.app_peer import get_warehouse_detail, get_employee_detail
from app.app_peer import update_employee_experience
from app.app_peer import get_specialist_employee_list


class TestCalcSolution(unittest.TestCase):
    def test_solution_1(self):
        # Add the print statement from your solution 1 to the empty string below
        self.assertEqual(
            read_database_version(),
            "PostgreSQL 11.18 on aarch64-unknown-linux-musl, compiled by gcc (Alpine 11.2.1_git20220219) 11.2.1 20220219, 64-bit",
        )

    def test_solution_2(self):
        # Add the print statements from your solution 2 to the empty string below
        self.assertEqual(get_warehouse_detail(2), (2, "Rewe Warehouse", 400))
        self.assertEqual(
            get_employee_detail(105),
            (
                105,
                "Linda",
                3,
                datetime.date(2004, 6, 4),
                "Logistics Spcialist",
                42000,
                None,
            ),
        )

    def test_solution_3(self):
        # Add the print statements from your solution 3 to the empty string below
        self.assertEqual(
            update_employee_experience(101),
            (101, "Mo", 1, datetime.date(2005, 2, 10), "HR Manager", 40000, 17),
        )

    def test_solution_4(self):
        # Add the print statements from your solution 4 to the empty string below
        self.assertEqual(
            get_specialist_employee_list("Driver", 30000),
            [
                (102, "Michael", 1, datetime.date(2018, 7, 23), "Driver", 30000, None),
                (108, "Karen", 4, datetime.date(2011, 10, 17), "Driver", 30000, None),
            ],
        )
