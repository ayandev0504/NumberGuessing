import tkinter as tk
import random

window = tk.Tk()
window.title("NUMBER GUESSING GAME")
window.geometry("400x300")

secret_number = random.randint(1 , 20)
attempts = 0

def check_guess():
    global attempts
    guess = int(entry.get())
    attempts += 1

    if guess < secret_number:
        result_label.config(text="Higher number please!")

    elif guess > secret_number:
        result_label.config(text="Lower number please!")

    else:
        result_label.config(text=f"Congratulations! You guessed it in {attempts} attempts! ")
        play_again_button.pack()
title_label = tk.Label(window, text="Welcome to Number Guessing Game!", font=("Arial", 14))
title_label.pack()

instruction_label = tk.Label(window, text="Guess a number between 1 and 20", font=("Arial", 12))
instruction_label.pack()

entry = tk.Entry(window)
entry.pack()

submit_button = tk.Button(window, text="Submit Guess", command=check_guess)
submit_button.pack()

result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack()

# Function to reset the game
def play_again():
    global secret_number, attempts
    secret_number = random.randint(1, 20)
    attempts = 0
    result_label.config(text="")
    play_again_button.pack_forget()  # Hide play again button after restarting the game

# Play again button
play_again_button = tk.Button(window, text="Play Again", command=play_again)
play_again_button.pack_forget()  # Initially hidden

# Run the Tkinter event loop
window.mainloop()