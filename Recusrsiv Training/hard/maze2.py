def is_solvable(maze, x, y, path):
    # base case: if the current position is the reward, return the path
    if maze[x][y] == 'X':
        return path

    # mark the current position as visited by replacing it with a wall
    maze[x] = maze[x][:y] + '#' + maze[x][y+1:]

    # recursive case: try to solve the maze by moving in each direction
    if x > 0 and maze[x-1][y] != '#':
        new_path = path + ["up"]
        result = is_solvable(maze, x-1, y, new_path)
        if result is not None:
            return result
    if x < len(maze)-1 and maze[x+1][y] != '#':
        new_path = path + ["down"]
        result = is_solvable(maze, x+1, y, new_path)
        if result is not None:
            return result
    if y > 0 and maze[x][y-1] != '#':
        new_path = path + ["left"]
        result = is_solvable(maze, x, y-1, new_path)
        if result is not None:
            return result
    if y < len(maze[0])-1 and maze[x][y+1] != '#':
        new_path = path + ["right"]
        result = is_solvable(maze, x, y+1, new_path)
        if result is not None:
            return result

    # if no direction leads to the reward, return None
    return None

def solve_maze(maze):
    # find the starting position
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                return is_solvable(maze, i, j, ["start:",(i, j)])


maze = [
    '----##',
    '-##--#',
    '--##-#',
    '#-#--#',
    '#-#-##',
    '--#-X#',
    '-#####',
    '-----S'
    ]

for i in maze:
    print(i)

path = solve_maze(maze)
if path is not None:
    print(path)
else:
    print("No solution found")
