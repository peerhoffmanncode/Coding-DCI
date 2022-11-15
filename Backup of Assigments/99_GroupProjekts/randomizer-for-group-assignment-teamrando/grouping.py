from typing import List
import random

STUDENTS = [
    "Alexander",
    "Badara",
    "Bahaa",
    "Dimi",
    "Emiley",
    "Fausto",
    "Felipe",
    "Jacques",
    "Lucas",
    "Michel",
    "Mirjam",
    "Muhannad",
    "Nadia",
    "Pasco",
    "Peer",
    "Reza",
    "Rico",
    "Shaban",
    "Somon",
    "Waheed",
    "Wessam",
    "Wojciech",
    "victor",
]


def group(student_list: List, group_size: int, team_names=[]) -> List[int]:
    if not team_names:
        raise Exception("Team names have to be present")
    number_of_students = len(student_list)
    number_of_teams = number_of_students // group_size
    student_group = []
    while True:
        try:
            team = random.sample(student_list, number_of_students // number_of_teams)
            student_group.append(team)
            for student in team:
                student_list = list(
                    filter(lambda s: s["name"] != student["name"], student_list)
                )
        except:
            break

    return student_group
