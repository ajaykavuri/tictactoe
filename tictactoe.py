"""
Tic Tac Toe Player
"""

import math
X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if terminal(board)[0]:
        return
    numX = 0
    numO = 0
    for row in board:
        for item in row:
            if item == X:
                numX += 1
            elif item == O:
                numO += 1
    if numX == numO:
        return 'X'
    return 'O'



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board)[0]:
        return None
    actionslist = []
    for i, row in enumerate(board):
        for j, item in enumerate(row):
            if item is None:
                actionslist.append((i, j))
    return actionslist


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception('action is not valid')
    else:
        play = player(board)
        newboard = [row[:] for row in board]
        newboard[action[0]][action[1]] = play
        return newboard



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if terminal(board)[1] == 'Tie':
        return None
    return terminal(board)[1]
    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    for row in board:
        if row[0] == row[1] == row[2] and not any(item is None for item in row):
            if row[0] == 'X':
                return (True, 'X')
            return (True, 'O')
    for i in range(3):
        if board[0][i] == board[1][i] == board [2][i] and board[0][i] is not None and board[1][i] is not None and board[2][i] is not None:
            if board[0][i] == 'X':
                return (True, 'X')
            return (True, 'O')
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None and board[1][1] is not None and board[2][2] is not None:
        if board[0][0] == 'X':
            return (True, 'X')
        return (True, 'O')
    if board[2][0] == board[1][1] == board[0][2] and board[2][0] is not None and board[1][1] is not None and board[0][2] is not None:
        if board[2][0] == 'X':
            return (True, 'X')
        return (True, 'O')
    if all([all(row) for row in board]):
        return (True, 'Tie')
    return (False, None)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    t = terminal(board)
    if t[0]:
        if t[1] == 'X':
            return 1
        elif t[1] == 'O':
            return -1
        else:
            return 0
    return 0

def maxvalue(board):
    """
    Returns the max utility and max action of the current state for the X player.
    """
    if terminal(board)[0]:
        return utility(board), None
    v = -math.inf
    maxaction = None
    for action in actions(board):
        minval = minvalue(result(board, action))
        if (minval[0] > v):
            v = minval[0]
            maxaction = action
    return (v, maxaction)

def minvalue(board):
    """
    Returns the min utility and min action of the current state for the O player.
    """
    if terminal(board)[0]:
        return utility(board), None
    v = math.inf
    minaction = None
    for action in actions(board):
        maxval = maxvalue(result(board, action))
        if (maxval[0] < v):
            v = maxval[0]
            minaction = action
    return (v, minaction)


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    currentPlayer = player(board)
    optimalaction = (-math.inf, -math.inf)
    if currentPlayer == 'X':
        optimalaction = maxvalue(board)[1]
    elif currentPlayer == 'O':
        optimalaction = minvalue(board)[1]
    return optimalaction
    

board2 = [[O, EMPTY, X], 
          [O, EMPTY, X], 
          [EMPTY, EMPTY, X]]
