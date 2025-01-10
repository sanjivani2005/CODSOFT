import tkinter as tk
from tkinter import messagebox
import random

# Game logic
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

def play_game(user_choice):
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    
    result = determine_winner(user_choice, computer_choice)
    
    result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")
    
    # Update scores
    global user_score, computer_score
    if "win" in result:
        user_score += 1
    elif "lose" in result:
        computer_score += 1
    
    score_label.config(text=f"User Score: {user_score}\nComputer Score: {computer_score}")

def play_again():
    result_label.config(text="")
    choice_label.config(text="Choose rock, paper, or scissors:")
    
def on_quit():
    root.quit()

# Initialize scores
user_score = 0
computer_score = 0

# Set up the main application window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")
root.geometry("400x400")
root.configure(bg="#f2f2f2")

# Title
title_label = tk.Label(root, text="Rock, Paper, Scissors", font=("Helvetica", 20, "bold"), bg="#f2f2f2", fg="#333333")
title_label.pack(pady=10)

# Choice label
choice_label = tk.Label(root, text="Choose rock, paper, or scissors:", font=("Helvetica", 14), bg="#f2f2f2", fg="#333333")
choice_label.pack(pady=5)

# Buttons for user choice
button_frame = tk.Frame(root, bg="#f2f2f2")
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", command=lambda: play_game("rock"), width=10, font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white")
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper", command=lambda: play_game("paper"), width=10, font=("Helvetica", 12, "bold"), bg="#2196F3", fg="white")
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: play_game("scissors"), width=10, font=("Helvetica", 12, "bold"), bg="#FF9800", fg="white")
scissors_button.grid(row=0, column=2, padx=10)

# Result label
result_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#f2f2f2", fg="#333333")
result_label.pack(pady=10)

# Score label
score_label = tk.Label(root, text=f"User Score: {user_score}\nComputer Score: {computer_score}", font=("Helvetica", 12), bg="#f2f2f2", fg="#333333")
score_label.pack(pady=5)

# Play again button
play_again_button = tk.Button(root, text="Play Again", command=play_again, width=20, font=("Helvetica", 12, "bold"), bg="#333333", fg="white")
play_again_button.pack(pady=5)

# Quit button
quit_button = tk.Button(root, text="Quit", command=on_quit, width=20, font=("Helvetica", 12, "bold"), bg="#f44336", fg="white")
quit_button.pack(pady=5)

# Run the application
root.mainloop()
