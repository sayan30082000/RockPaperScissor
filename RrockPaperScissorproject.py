import random
import tkinter as tk
from tkinter import messagebox

def get_computer_choice():
    """Get a random choice for the computer."""
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the game."""
    if user_choice == computer_choice:
        return "It's a tie!"

    # Winning combinations for the user
    if (user_choice == "Rock" and computer_choice == "Scissors") or \
       (user_choice == "Paper" and computer_choice == "Rock") or \
       (user_choice == "Scissors" and computer_choice == "Paper"):
        return "You win!"

    return "Computer wins!"

def play(user_choice):
    """Play a round of Rock, Paper, Scissors."""
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)

    messagebox.showinfo("Result", f"You chose: {user_choice}\nComputer chose: {computer_choice}\n\n{result}")

def main():
    """Main function to set up the GUI."""
    root = tk.Tk()
    root.title("Rock, Paper, Scissors")
    root.configure(bg="#e6f7ff")  # Light blue background

    tk.Label(root, text="Choose one:", font=("Arial", 16), bg="#e6f7ff", fg="#003366").pack(pady=10)

    button_frame = tk.Frame(root, bg="#e6f7ff")
    button_frame.pack(pady=20)

    tk.Button(button_frame, text="Rock", font=("Arial", 14), width=10, bg="#4da6ff", fg="white", command=lambda: play("Rock")).grid(row=0, column=0, padx=10)
    tk.Button(button_frame, text="Paper", font=("Arial", 14), width=10, bg="#4da6ff", fg="white", command=lambda: play("Paper")).grid(row=0, column=1, padx=10)
    tk.Button(button_frame, text="Scissors", font=("Arial", 14), width=10, bg="#4da6ff", fg="white", command=lambda: play("Scissors")).grid(row=0, column=2, padx=10)

    tk.Button(root, text="Quit", font=("Arial", 14), bg="#4da6ff", fg="white", command=root.quit).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
