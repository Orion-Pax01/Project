import tkinter as tk
from tkinter import messagebox

# Initialize the game variables
current_player = "X"
board = [" " for _ in range(9)]
score = {"X": 0, "O": 0}

# Function to check if there's a winner
def check_winner():
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6)]

    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return True
    return False

# Function to handle a player's move
# Function to handle a player's move
def player_move(position):
    global current_player

    if board[position] == " ":
        board[position] = current_player
        buttons[position].config(text=current_player)

        if check_winner():
            messagebox.showinfo("Tic-Tac-Toe", f"Player {current_player} wins!")
            score[current_player] += 1
            update_score()
            reset_game()
        elif " " not in board:
            messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"

        # Add logic for "O" player's move here
        if current_player == "O":
            # You can implement AI or player logic for "O" here
            # For simplicity, let's assume "O" places its symbol in the first empty cell
            for i in range(9):
                if board[i] == " ":
                    player_move(i)  # Recursively call player_move for "O"
                    break

# Function to reset the game
def reset_game():
    global board, current_player
    board = [" " for _ in range(9)]
    current_player = "X"
    for button in buttons:
        button.config(text=" ")
    update_score()

# Function to update the score display
def update_score():
    score_label.config(text=f"Player X: {score['X']}  Player O: {score['O']}")

# Create the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Create the buttons for the game board
buttons = []
for i in range(9):
    button = tk.Button(root, text=" ", width=10, height=3, command=lambda i=i: player_move(i))
    buttons.append(button)
    button.grid(row=i // 3, column=i % 3)

# Create a label to display the score
score_label = tk.Label(root, text="Player X: 0  Player O: 0")
score_label.grid(row=3, column=0, columnspan=3)

# Create a New Game button
new_game_button = tk.Button(root, text="New Game", command=reset_game)
new_game_button.grid(row=4, column=0, columnspan=3)

# Run the game
root.mainloop()
