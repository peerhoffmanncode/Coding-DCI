def get(data, path):
    ''' recursive function to find nested data in a give datatype
        data is the datatype
        path is the path to the value to find
        '''
    parsing_list = path.split(".")
    p = parsing_list[0]

    if str(p).isdigit():
        p = int(p)

    if len(parsing_list) > 1:
        result = get(data[p], ".".join(parsing_list[1:]))
    else:
        result = data[p]
    return result

### Test cases

data = {
  'students': [
    {
      'name': 'Josephine',
      'subjects': [
        {
          'name': 'English',
          'teacher': 'Mr. Hoover'
        }
      ]
    },
    {
      'name': 'Luke',
      'subjects': [
        {
          'name': 'History',
          'teacher': 'Mrs. Peters'
        }
      ]
    },
    {
      'name': 'Julia',
      'subjects': [
        {
          'name': 'Chemistry',
          'teacher': 'Mrs. Fauci'
        }
      ]
    }
  ]
}

print(get(data, 'students.1.subjects.0.name'))
print(get(data, 'students.0.subjects.0.teacher'))