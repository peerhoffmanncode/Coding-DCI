def is_solvable(maze, x, y):
    # base case: if the current position is the reward, return True
    if maze[x][y] == 'X':
        return True

    # mark the current position as visited by replacing it with a wall
    maze[x] = maze[x][:y] + '#' + maze[x][y+1:]

    # recursive case: try to solve the maze by moving in each direction
    if x > 0 and maze[x-1][y] != '#' and is_solvable(maze, x-1, y):
        return True
    if x < len(maze)-1 and maze[x+1][y] != '#' and is_solvable(maze, x+1, y):
        return True
    if y > 0 and maze[x][y-1] != '#' and is_solvable(maze, x, y-1):
        return True
    if y < len(maze[0])-1 and maze[x][y+1] != '#' and is_solvable(maze, x, y+1):
        return True

    # if no direction leads to the reward, return False
    return False

def solve_maze(maze):
    # find the starting position
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                return is_solvable(maze, i, j)


maze = [
    '----##',
    'X#-#-#',
    '#--###',
    '-----S'
    ]

print(solve_maze(maze))
