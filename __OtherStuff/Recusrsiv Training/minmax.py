import math

# utility function to evaluate the current state of the game
def evaluate(board):
    # check for a horizontal win
    for i in range(len(board)):
        for j in range(len(board[0]) - 3):
            if board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3] and board[i][j] != ' ':
                if board[i][j] == 'X':
                    return 1
                else:
                    return -1

    # check for a vertical win
    for i in range(len(board) - 3):
        for j in range(len(board[0])):
            if board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j] and board[i][j] != ' ':
                if board[i][j] == 'X':
                    return 1
                else:
                    return -1

    # check for a diagonal win (top left to bottom right)
    for i in range(len(board) - 3):
        for j in range(len(board[0]) - 3):
            if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] and board[i][j] != ' ':
                if board[i][j] == 'X':
                    return 1
                else:
                    return -1

    # check for a diagonal win (top right to bottom left)
    for i in range(len(board) - 3):
        for j in range(3, len(board[0])):
            if board[i][j] == board[i+1][j-1] == board[i+2][j-2] == board[i+3][j-3] and board[i][j] != ' ':
                if board[i][j] == 'X':
                        return 1
                else:
                        return -1

    # if the game is a draw, return 0
    return 0

# minimax function to find the optimal move for the current player
def minimax(board, depth, player, alpha, beta):
    # base case: if the game has been won or is a draw, return the evaluation
    result = evaluate(board)
    if result != 0:
        return result

    # recursive case: try all possible moves and choose the optimal one
    if player == 'X':
        max_score = -math.inf
        for j in range(len(board[0])):
            # find the first empty space in the column
            i = len(board) - 1
            while i >= 0 and board[i][j] != ' ':
                i -= 1
            # if the column is full, skip it
            if i < 0:
                continue
            # try the move and update the maximum score
            board[i][j] = 'X'
            score = minimax(board, depth+1, 'O', alpha, beta)
            board[i][j] = ' '
            max_score = max(max_score, score)
            alpha = max(alpha, score)
            # if the maximum score is greater than or equal to beta, return it
            if max_score >= beta:
                return max_score
        return max_score
    else:
        min_score = math.inf
        for j in range(len(board[0])):
            # find the first empty space in the column
            i = len(board) - 1
            while i >= 0 and board[i][j] != ' ':
                i -= 1
            # if the column is full, skip it
            if i < 0:
                continue
            # try the move and update the minimum score
            board[i][j] = 'O'
            score = minimax(board, depth+1, 'X', alpha, beta)
            board[i][j] = ' '
            min_score = min(min_score, score)
            beta = min(beta, score)
            # if the minimum score is less than or equal to alpha, return it
            if min_score <= alpha:
                return min_score
        return min_score

    # function to find the optimal move for the current player
def find_move(board, player):
    best_move = -1
    if player == 'X':
        max_score = -math.inf
    for j in range(len(board[0])):
        # find the first empty space in the column
        i = len(board) - 1
        while i >= 0 and board[i][j] != ' ':
            i -= 1
        # if the column is full, skip it
        if i < 0:
            continue
        # try the move and update the best move and maximum score
        board[i][j] = 'X'
        score = minimax(board, 0, 'O', -math.inf, math.inf)
        board[i][j] = ' '
        if score > max_score:
            max_score = score
            best_move = j
    return best_move

# example usage
board = [
    [' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', 'X', ' ', ' '],
    [' ', ' ', 'O', 'O', 'X', ' ']
]

move = find_move(board, 'X')
print(move)  # should print the optimal move for player X
