def friends(g, person_id, visited=None):
    if visited is None:
        visited = set()
    visited.add(person_id)
    for friend_id in g[person_id]:
        if friend_id not in visited:
            visited.update(friends(g, friend_id, visited))
    return visited

g = {
    1: [2,3],    # 1 is friends with 2 and 3
    2: [1],      # 2 is friends with 1
    3: [1,4],    # 3 is friends with 1 and 4
    4: [3],      # etc
    5: [6],
    6: [5,7],
    7: [6]
}

for i in g:
    print(friends(g,i))
