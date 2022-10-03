def kick_da_student(dataset: list) -> list:
    ''' function to remove students with 
        more, or !two! F grade '''
    work_list = []
    for idx, student in enumerate(dataset):
        f_garde = 0
        for subjects in student["subjects"]:
            if subjects["grade"] == "F":
                f_garde += 1
        if f_garde < 2:
            work_list.append(dataset[idx])
    return work_list

### Data give
students = [
  {
    'name': 'Peter', 
    'subjects': [
      {'name': 'English', 'grade': 'A'},
      {'name': 'German', 'grade': 'C'},
      {'name': 'Maths', 'grade': 'B'}
    ]
  },
  {
    'name': 'Robin', 
    'subjects': [
      {'name': 'English', 'grade': 'D'},
      {'name': 'German', 'grade': 'B'},
      {'name': 'Maths', 'grade': 'B'}
    ]
  },
  {
    'name': 'Michael', 
    'subjects': [
      {'name': 'English', 'grade': 'A'},
      {'name': 'German', 'grade': 'F'},
      {'name': 'Maths', 'grade': 'F'}
    ]
  },
]

# Execute test
change_students_list = kick_da_student(students)
print(change_students_list)
