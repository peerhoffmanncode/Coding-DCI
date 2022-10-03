def get(data, path):
    ''' function to pars down to a given path '''
    # copy data to safe in global scope
    work = data.copy()
    pars_lst = path.split(".")
    #p = pars_lst[0]
    for p in pars_lst:
        # p holds current segment of the path
        if str(p).isdigit():
            p = int(p)
        # subset of datatype(list/dict) will be new datatye(list/dict) now
        work = work[p]
    # return item(s)!
    return work


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