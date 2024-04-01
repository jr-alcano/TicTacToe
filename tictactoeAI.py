from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.title('Tic-Tac-Toe')

# X will start so starts as true, False means O goes
clicked = True
count = 0
winner = False


def is_draw():
    return all(b["text"] != " " for b in [b1, b2, b3, b4, b5, b6, b7, b8, b9])


# disable the buttons
def disable_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)


def minimax(isMaximizing):
    score = win_minimax()  # Assumed to check the board's state and return 10, -10, or 0

    if score == 10 or score == -10:
        return score

    if is_draw():
        return 0

    if isMaximizing:
        bestScore = -float('inf')
        for b in [b1, b2, b3, b4, b5, b6, b7, b8, b9]:
            if b["text"] == " ":
                b["text"] = "O"  # Simulate AI move
                score = minimax(False)
                b["text"] = " "  # Undo the move
                bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore = float('inf')
        for b in [b1, b2, b3, b4, b5, b6, b7, b8, b9]:
            if b["text"] == " ":
                b["text"] = "X"  # Simulate human move
                score = minimax(True)
                b["text"] = " "  # Undo the move
                bestScore = min(score, bestScore)
        return bestScore


def ai_move():
    global clicked, count

    bestScore = -float('inf')
    bestMove = None

    # Iterate through all buttons to find the best move
    for b in (b1, b2, b3, b4, b5, b6, b7, b8, b9):
        if b["text"] == " ":
            b["text"] = "O"  # Make the move temporarily
            score = minimax(False)  # Call minimax assuming the next player (human) minimizes the score
            b["text"] = " "  # Undo the move

            # Update the best score and move if current move is better
            if score > bestScore:
                bestScore = score
                bestMove = b

    # Perform the best move
    if bestMove:
        bestMove["text"] = "O"
        clicked = True
        count += 1
        won()


# separate check win function for minimax eval, no messageboxes
def win_minimax():
    # Across win conditions
    if b1["text"] == b2["text"] and b2["text"] == b3["text"] and b1["text"] != " ":

        if b1["text"] == "X":
            return -10
        else:
            return 10
    elif b4["text"] == b5["text"] and b5["text"] == b6["text"] and b4["text"] != " ":

        if b4["text"] == "X":
            return -10
        else:
            return 10
    elif b7["text"] == b8["text"] and b8["text"] == b9["text"] and b7["text"] != " ":

        if b7["text"] == "X":
            return -10
        else:
            return 10

    # column win conditions
    elif b1["text"] == b4["text"] and b4["text"] == b7["text"] and b1["text"] != " ":

        if b1["text"] == "X":
            return -10
        else:
            return 10
    elif b2["text"] == b5["text"] and b5["text"] == b8["text"] and b2["text"] != " ":

        if b2["text"] == "X":
            return -10
        else:
            return 10
    elif b3["text"] == b6["text"] and b6["text"] == b9["text"] and b3["text"] != " ":

        if b3["text"] == "X":
            return -10
        else:
            return 10

    # diagonal win conditions
    elif b1["text"] == b5["text"] and b5["text"] == b9["text"] and b1["text"] != " ":

        if b1["text"] == "X":
            return -10
        else:
            return 10
    elif b3["text"] == b5["text"] and b5["text"] == b7["text"] and b3["text"] != " ":

        if b3["text"] == "X":
            return -10
        else:
            return 10
    return 0


# check to win for actual end of game
def won():
    global winner
    winner = False
    # Across win conditions
    if b1["text"] == b2["text"] and b2["text"] == b3["text"] and b1["text"] != " ":
        winner = True
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        if b1["text"] == "X":
            messagebox.showinfo("Tic Tac Toe", "X wins")
        else:
            messagebox.showinfo("Tic Tac Toe", "O wins")
        disable_buttons()
    elif b4["text"] == b5["text"] and b5["text"] == b6["text"] and b4["text"] != " ":
        winner = True
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        if b4["text"] == "X":
            messagebox.showinfo("Tic Tac Toe", "X wins")
        else:
            messagebox.showinfo("Tic Tac Toe", "O wins")
        disable_buttons()
    elif b7["text"] == b8["text"] and b8["text"] == b9["text"] and b7["text"] != " ":
        winner = True
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        if b7["text"] == "X":
            messagebox.showinfo("Tic Tac Toe", "X wins")
        else:
            messagebox.showinfo("Tic Tac Toe", "O wins")
        disable_buttons()

    # column win conditions
    elif b1["text"] == b4["text"] and b4["text"] == b7["text"] and b1["text"] != " ":
        winner = True
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        if b1["text"] == "X":
            messagebox.showinfo("Tic Tac Toe", "X wins")
        else:
            messagebox.showinfo("Tic Tac Toe", "O wins")
        disable_buttons()
    elif b2["text"] == b5["text"] and b5["text"] == b8["text"] and b2["text"] != " ":
        winner = True
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        if b2["text"] == "X":
            messagebox.showinfo("Tic Tac Toe", "X wins")
        else:
            messagebox.showinfo("Tic Tac Toe", "O wins")
        disable_buttons()
    elif b3["text"] == b6["text"] and b6["text"] == b9["text"] and b3["text"] != " ":
        winner = True
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        if b3["text"] == "X":
            messagebox.showinfo("Tic Tac Toe", "X wins")
        else:
            messagebox.showinfo("Tic Tac Toe", "O wins")
        disable_buttons()

    # diagonal win conditions
    elif b1["text"] == b5["text"] and b5["text"] == b9["text"] and b1["text"] != " ":
        winner = True
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        if b1["text"] == "X":
            messagebox.showinfo("Tic Tac Toe", "X wins")
        else:
            messagebox.showinfo("Tic Tac Toe", "O wins")
        disable_buttons()
    elif b3["text"] == b5["text"] and b5["text"] == b7["text"] and b3["text"] != " ":
        winner = True
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        if b3["text"] == "X":
            messagebox.showinfo("Tic Tac Toe", "X wins")
        else:
            messagebox.showinfo("Tic Tac Toe", "O wins")
        disable_buttons()


# button clicked function
def b_click(b):  # b parameter is a button
    global clicked, count, winner
    if is_draw():
        messagebox.showinfo("Tic Tac Toe", "Draw, no one wins")
    if b["text"] == " " and clicked == True:  # X case
        b["text"] = "X"
        clicked = False
        count += 1
        won()
        if winner == False:
            b.after(500, ai_move)
            if is_draw():
                messagebox.showinfo("Tic Tac Toe", "Draw, no one wins")
    # elif b["text"] == " " and clicked == False:  # O case
    #   b["text"] = "O"
    #  clicked = True
    # count += 1
    # won()
    # else:
    #   messagebox.showerror("Tic Tac Toe", "Box is filled\nPick another box")


# buttons
b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: b_click(b1))
b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: b_click(b2))
b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: b_click(b3))

b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: b_click(b4))
b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: b_click(b5))
b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: b_click(b6))

b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: b_click(b7))
b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: b_click(b8))
b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: b_click(b9))

# grid the buttons
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)

root.mainloop()
