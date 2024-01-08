#!/usr/bin/env python
# coding: utf-8

# In[7]:


def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def is_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)): 
            #checking rows and columns
            return True
        if all(board[i][i] == player for i in range(3)) or  all(board[i][2 - i] == player for i in range(3)):     
            #checking both the diagonals
            return True
    return False

def is_full(board):
    # Check if the board is full
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def get_empty_cells(board):
    # Get the list of empty cells
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def evaluate(board):
    # Evaluate the current state of the board
    if is_winner(board, 'X'):
        return -1
    elif is_winner(board, 'O'):
        return 1
    elif is_full(board):
        return 0
    else:
        return None

def minimax(board, depth, maximizing_player):
    score = evaluate(board)

    if score is not None:
        return score

    if maximizing_player:
        max_eval = -2 # since the least value of score is -1
        for i, j in get_empty_cells(board):
            board[i][j] = 'O'
            eval = minimax(board, depth + 1, False)
            board[i][j] = ' '
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = 2 # since the max value of score is 1
        for i, j in get_empty_cells(board):
            board[i][j] = 'X'
            eval = minimax(board, depth + 1, True)
            board[i][j] = ' '
            min_eval = min(min_eval, eval)
        return min_eval

def best_move(board):
    best_val = float('-inf')
    best_move = (-1, -1)

    for i, j in get_empty_cells(board):
        board[i][j] = 'O'
        move_val = minimax(board, 0, False)
        board[i][j] = ' '

        if move_val > best_val:
            best_move = (i, j)
            best_val = move_val

    return best_move

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    turn = 'X'

    while True:
        print_board(board)

        if turn == 'X':
            print("Player's turn (X)")
            row = int(input("Enter row (0, 1, or 2): "))
            if row>2 or row<0:
                print("please enter a valid row number")
                continue
            col = int(input("Enter column (0, 1, or 2): "))
            if col>2 or col<0:
                print("please enter a valid column number")
                continue
            if board[row][col] == ' ':
                board[row][col] = 'X'
            else:
                print("Cell already occupied. Try again.")
                continue
        else:
            print("Computer's turn (O)")
            row, col = best_move(board)
            board[row][col] = 'O'

        if is_winner(board, turn):
            print_board(board)
            print(f"{turn} wins!")
            break
        elif is_full(board):
            print_board(board)
            print("It's a tie!")
            break

        turn = 'O' if turn == 'X' else 'X'

play_game()


# In[ ]:




