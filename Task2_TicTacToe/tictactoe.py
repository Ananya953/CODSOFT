import math

# Initialize board
board = [' ' for _ in range(9)]

# Print the board
def print_board():
    print()
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')
    print()

# Check for winner
def check_winner(brd, player):
    win_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combo in win_combos:
        if all(brd[i] == player for i in combo):
            return True
    return False

# Check for draw
def is_draw(brd):
    return ' ' not in brd

# Minimax algorithm
def minimax(brd, is_maximizing):
    if check_winner(brd, 'O'):
        return 1
    elif check_winner(brd, 'X'):
        return -1
    elif is_draw(brd):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if brd[i] == ' ':
                brd[i] = 'O'
                score = minimax(brd, False)
                brd[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if brd[i] == ' ':
                brd[i] = 'X'
                score = minimax(brd, True)
                brd[i] = ' '
                best_score = min(score, best_score)
        return best_score

# Best move for AI
def best_move():
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    board[move] = 'O'

# Main game
def play():
    print("Welcome to Tic Tac Toe AI")
    print("You are X, AI is O")
    print_board()

    while True:
        # Human move
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] != ' ':
                print("Invalid move! Try again.")
                continue
        except:
            print("Please enter a valid number (1-9)")
            continue

        board[move] = 'X'
        print_board()

        if check_winner(board, 'X'):
            print("🎉 You win!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

        # AI move
        print("AI is making a move...")
        best_move()
        print_board()

        if check_winner(board, 'O'):
            print("AI wins!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

play()