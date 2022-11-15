from grouping import group

students = [
    {"name": "Student 1", "score": 50},
    {"name": "Student 2", "score": 60},
    {"name": "Student 3", "score": 20},
    {"name": "Student 4", "score": 36},
    {"name": "Student 5", "score": 41},
    {"name": "Student 6", "score": 50},
]


def test_matching():
    # from 6 students, we can get 2 teams
    assert len(group(students, group_size=3, team_names=["A", "B", "C"])) == 2

    # from 6 students, we can get 3 teams with 2
    assert len(group(students, group_size=2, team_names=["A", "B", "C"])) == 3

    assert len(group(students, group_size=1, team_names=["A", "B", "C"])) == 6
