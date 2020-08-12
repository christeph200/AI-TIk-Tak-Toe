#"""
#Tic Tac Toe Player
#"""
#
#import math
#import copy
#X = "X"
#O = "O"
#EMPTY = None
#
#
#def initial_state():
#    """
#    Returns starting state of the board.
#    """
#    return [[EMPTY, EMPTY, EMPTY],
#            [EMPTY, EMPTY, EMPTY],
#            [EMPTY, EMPTY, EMPTY]]
#
#
#def player(board):
#    """
#    Returns player who has the next turn on a board.
#    """
#    # start counting the number of X and O
#    nX = 0
#    nO = 0
#
#    nX=board[0].count(X)+board[1].count(X)+board[2].count(X)
#    nO=board[0].count(O)+board[1].count(O)+board[2].count(O)
#
#    # if X goes first, number of X > number of O, then it's O's turn
#    # if then O goes after, number of O == number of X and if not terminal state,
#    # then it's X's turn
#
#    
#        
#    
#    if nX==nO:
#        return X
#    else:
#        return O
#    
#        
#    
#
#
#def actions(board):
#    """
#    Returns set of all possible actions (i, j) available on the board.
#    """
#    k=[]
#    for i in range(3):
#        for j in range(3):
#            if board[i][j]==EMPTY:
#                k.append([i,j])
#    return k
#    
#    
#
#
#def result(board, action):
#    """
#    Returns the board that results from making move (i, j) on the board.
#    """
#    
#    copyboard=copy.deepcopy(board)
##    try:
##        if(copyboard[action[0],action[1]]!=EMPTY):
##            raise IndexError
##        else:
##            copyboard[action[0],action[1]]=player(copyboard)
##            return copyboard
##    except IndexError:
##        print('spot occupied already')
#    
#    copyboard[action[0]][action[1]] = player(copyboard)
#    return copyboard
#
#def winner(board):
#    """
#    Returns the winner of the game, if there is one.
#    """
#    for i in range(3):
#        count1=0
#        count2=0
#        for j in range(3):
#            if board[j][i]==X:
#                count1+=1
#            elif(board[j][i]==O):
#                count2+=1
#            if count1==3:
#                return X
#            if count2==3:
#                return O 
#    if(board[0].count(X)==3 or board[1].count(X)==3 or board[2].count(X)==3):
#        return X
#    elif(board[0].count(O)==3 or board[1].count(O)==3 or board[2].count(O)==3):
#        return O
#    elif(board[0][0]==X and board[1][1]==X and board[2][2]==X):
#        return X
#    elif(board[0][0]==O and board[1][1]==O and board[2][2]==O):
#        return O
#    elif(board[0][2]==X and board[1][1]==X and board[2][0]==X):
#        return X
#    elif(board[0][2]==O and board[1][1]==O and board[2][0]==O):
#        return O
#    else:
#        return None
#    
#    
#
#def terminal(board):
#    """
#    Returns True if game is over, False otherwise.
#    """
#    k=winner(board)
#    if(k==X or k==O):
#        return True
#    elif(board[0].count(EMPTY)==0 and board[1].count(EMPTY)==0 and board[2].count(EMPTY)==0):
#        return True
#    elif(k==None):
#        return False
#
#
#def utility(board):
#    """
#    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
#    """
#    if(winner(board)==X):
#        return 1
#    elif(winner(board)==O):
#        return -1
#    elif(winner(board)==None):
#        return 0
#
##def minimax(board):
##    """
##    Returns the optimal action for the current player on the board.
##    """
##    currentplayer=player(board)
##    
##    if currentplayer==X:
##        v=-math.inf
##        for action in actions(board):
##            p=minivalue(result(board,action))
##            if p>v:
##                v=p
##                best=action
##    else:
##        v=math.inf
##        for action in actions(board):
##            p=maxvalue(result(board,action))
##            if p<v:
##                v=p
##                best=action
##    return best
##    
##def maxvalue(board):
##        if terminal(board):
##            return utility(board)
##        k=-math.inf
##    
##        for action in actions(board):
##            
##            v=max(v,minivalue(result(board,action)))
##            
##        return k
##        
##    
##def minivalue(board):
##        
##        if terminal(board):
##            return utility(board)
##    
##        k=math.inf
##        for action in actions(board):
##            
##            v=min(v,maxvalue(result(board,action)))
##            
##        return k
#        
#def minimax(board):
#    """
#    Returns the optimal action for the current player on the board.
#    """
#    current_player = player(board)
#
#    if current_player == X:
#        v = -math.inf
#        for action in actions(board):
#            k = min_value(result(board, action))
#            if k > v:
#                v = k
#                best_move = action
#    else:
#        v = math.inf
#        for action in actions(board):
#            k = max_value(result(board, action))
#            if k < v:
#                v = k
#                best_move = action
#    return best_move
#
#def max_value(board):
#    if terminal(board):
#        return utility(board)
#    v = -math.inf
#    for action in actions(board):
#        v = max(v, min_value(result(board, action)))
#    return v
#
#def min_value(board):
#    if terminal(board):
#        return utility(board)
#    v = math.inf
#    for action in actions(board):
#        v = min(v, max_value(result(board, action)))
#    return v
#        
#        
#        
#        
#        
#        
#        
#      



"""
Tic Tac Toe Player
"""
import copy
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
    x_count = 0
    o_count = 0

    for rows in board:
        for columns in rows:
            if columns == X:
                x_count += 1
            elif columns == O:
                o_count += 1
    if x_count <= o_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    if new_board[action[0]][action[1]] != EMPTY:
        return Exception
    else:
        new_board[action[0]][action[1]] = player(board)

    return new_board
    # if action in actions(board):
    #     (i, j) = action
    #     current_player = player(board)
    #     new_board = copy.deepcopy(board)
    #     new_board[i][j] = current_player
    #     return new_board
    # else:
    #     raise Exception


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == X:
            return X
        elif board[i][0] == board[i][1] == board[i][2] == O:
            return O
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == X:
            return X
        elif board[0][i] == board[1][i] == board[2][i] == O:
            return O

    if board[0][0] == board[1][1] == board[2][2] == X:
        return X
    if board[0][0] == board[1][1] == board[2][2] == O:
        return O
    if board[0][2] == board[1][1] == board[2][0] == X:
        return X
    if board[0][2] == board[1][1] == board[2][0] == O:
        return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        return True
    else:
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    return False
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == X:
        score = -math.inf
        best = None

        for action in actions(board):
            current = min_value(result(board, action))
            if current > score:
                score = current
                best = action
        return best

    elif player(board) == O:
        score = math.inf
        best = None
        for action in actions(board):
            current = max_value(result(board, action))
            if current < score:
                score = current
                best = action
        return best


def max_value(board):
    if terminal(board):
        return utility(board)

    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))

    return v


def min_value(board):
    if terminal(board):
        return utility(board)

    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))

    return v