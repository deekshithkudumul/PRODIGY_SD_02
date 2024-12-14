import random
import tkinter as tk
from tkinter import ttk, messagebox

class GuessTheNumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess The Number Game")
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.guess_history = []

        # Create and place the instruction label
        self.instruction_label = ttk.Label(root, text="I'm thinking of a number between 1 and 100. Can you guess it?")
        self.instruction_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Create and place the entry field for user's guess
        self.guess_entry = ttk.Entry(root)
        self.guess_entry.grid(row=1, column=0, padx=10, pady=10)

        # Create and place the guess button
        self.guess_button = ttk.Button(root, text="Guess", command=self.check_guess)
        self.guess_button.grid(row=1, column=1, padx=10, pady=10)

        # Create and place the result label
        self.result_label = ttk.Label(root, text="")
        self.result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Create and place the Listbox for guess history
        self.history_label = ttk.Label(root, text="Guess History:")
        self.history_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        self.history_listbox = tk.Listbox(root, height=10, width=50)
        self.history_listbox.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def check_guess(self):
        guess = self.guess_entry.get()
        try:
            guess = int(guess)
        except ValueError:
            messagebox.showerror("Invalid Input", "That's not a valid number. Please try again.")
            self.guess_entry.delete(0, tk.END)  # Clear the entry field
            return

        self.attempts += 1
        self.guess_history.append(guess)
        self.history_listbox.insert(tk.END, f"Attempt {self.attempts}: {guess}")

        if guess < self.number_to_guess:
            self.result_label.config(text=f"The number is greater than {guess}.")
        elif guess > self.number_to_guess:
            self.result_label.config(text=f"The number is less than {guess}.")
        else:
            messagebox.showinfo("Congratulations!", f"You guessed the number in {self.attempts} attempts.")
            self.reset_game()

        self.guess_entry.delete(0, tk.END)  # Clear the entry field after each guess

    def reset_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.guess_history = []
        self.guess_entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.instruction_label.config(text="I'm thinking of a number between 1 and 100. Can you guess it?")
        self.history_listbox.delete(0, tk.END)

# Create the main window
root = tk.Tk()
game = GuessTheNumberGame(root)

# Run the application
root.mainloop()
