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

def get(data, key):
  keys = key.split('.')
  value = data
  for key in keys:
    if key.isdigit():
      key = int(key)

    try:
      value = value[key]
    except Exception as e:
      return None

  return(value)

def main():
    print(get(data, 'students.1.subjects.0.name'))
    print(get(data, 'students.0.subjects.0.teacher'))


if __name__ == "__main__":
    main()