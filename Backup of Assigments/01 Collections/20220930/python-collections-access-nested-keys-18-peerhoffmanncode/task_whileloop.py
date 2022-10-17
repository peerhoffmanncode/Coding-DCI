def get(work, path):
    ''' function to find nested data in a give datatype
        data is the datatype
        path is the path to the value to find
        '''
    pars_list = path.split(".")
    #p = pars_lst[0]
    for node in pars_list:
        # p holds current segment of the path
        if str(node).isdigit():
            node = int(node)
        # subset of datatype(list/dict) will be new datatype(list/dict) now
        work = work[node]
    # return item(s)!
    return work


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