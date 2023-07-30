import tkinter as tk
from tkinter import messagebox

# Function to check if there is a winner
def check_winner():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    return None

# Function to handle button clicks
def on_click(row, col):
    global player, winner
    if board[row][col] == "" and not winner:
        board[row][col] = player
        buttons[row][col].config(text=player, state=tk.DISABLED)
        winner = check_winner()
        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            root.quit()
        elif all(board[i][j] != "" for i in range(3) for j in range(3)):
            messagebox.showinfo("Game Over", "It's a draw!")
            root.quit()
        else:
            player = "X" if player == "O" else "O"

# Create the main window
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("300x300")

# Create the game board
board = [["" for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]

# Create the buttons for the game board
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", font=("Arial", 40), width=2, height=1,
                                  command=lambda row=i, col=j: on_click(row, col))
        buttons[i][j].grid(row=i, column=j, padx=5, pady=5)

player = "X"  # Starting player is X
winner = None

root.mainloop()
