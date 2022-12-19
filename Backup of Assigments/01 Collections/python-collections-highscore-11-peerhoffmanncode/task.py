
def get_score(name: str, data: dict) -> str:
    ''' fuction to get a score of a given participants'''
    if name.lower() in list(data.keys()):
        return f"{name} scored {data[name.lower()]} points"
    return f"{name} did not participate"

participants = ['Brian', 'Britney', 'Ben']
scores = {
  'brian': 25,
  'britney': 80,
  'ben': 50
}

# changed the call two 2 args, relay on global scope is uncool
print(get_score('Paul', scores))
print(get_score('Britney', scores))

# 2nd test - all cases from list
for p in participants:
    print(get_score(p, scores))