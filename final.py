import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock Paper Scissors Game")
        self.master.geometry("550x400")  # Fixed frame size
        self.master.configure(bg='#F5F5F5')  # Set light gray background color

        self.user_score = 0
        self.computer_score = 0

        # Frame 1 - Title and Instructions
        self.frame1 = tk.Frame(master, bg='#F5F5F5')
        self.frame1.grid(row=0, column=0, columnspan=3, pady=10)  # Centered
        title_label = tk.Label(self.frame1, text="Rock Paper Scissors Game", font=("Helvetica", 20, "bold", "underline"), bg='#F5F5F5', fg='black')
        title_label.pack()
        instructions_label = tk.Label(self.frame1, text="Choose Rock, Paper, or Scissors and click Play.", font=("Helvetica", 12), bg='#F5F5F5', fg='black')
        instructions_label.pack()

        # Frame 2 - User and Computer Choices
        self.frame2 = tk.Frame(master, bg='#F5F5F5')
        self.frame2.grid(row=1, column=0, columnspan=3, pady=10)  # Centered
        self.user_choice_label = tk.Label(self.frame2, text="Your Choice:", font=("Helvetica", 14), bg='#F5F5F5', fg='black')
        self.user_choice_label.pack(side=tk.LEFT, padx=10, anchor='w')  # Anchored to the left
        self.computer_choice_label = tk.Label(self.frame2, text="Computer's Choice:", font=("Helvetica", 14), bg='#F5F5F5', fg='black')
        self.computer_choice_label.pack(side=tk.LEFT, padx=10, anchor='w')  # Anchored to the left

        # Frame 3 - Result Display
        self.frame3 = tk.Frame(master, bg='#F5F5F5')
        self.frame3.grid(row=2, column=0, columnspan=3, pady=10)  # Centered
        self.result_label = tk.Label(self.frame3, text="", font=("Helvetica", 18), bg='#F5F5F5', fg='black')
        self.result_label.pack(anchor='center')

        # Frame 4 - User Choice Buttons
        self.frame4 = tk.Frame(master, bg='#F5F5F5')
        self.frame4.grid(row=3, column=0, pady=10)  # Centered
        choices = ["Rock", "Paper", "Scissors"]
        for choice in choices:
            button_color = '#D2B48C' if choice == 'Rock' else '#ADD8E6' if choice == 'Paper' else '#C0C0C0'  # Light brown, light blue, silver
            button = tk.Button(self.frame4, text=choice, font=("Helvetica", 12), width=10, bg=button_color, fg='black', command=lambda c=choice: self.set_user_choice(c))
            button.pack(side=tk.LEFT, padx=10, anchor='w')  # Anchored to the left

        # Frame 5 - Score Frame
        self.frame5 = tk.Frame(master, bg='#F5F5F5')
        self.frame5.grid(row=4, column=0, columnspan=3, pady=10)  # Centered
        self.user_score_button = tk.Button(self.frame5, text=f"User Score: {self.user_score}", font=("Helvetica", 12), width=15, bg='#87CEFA', fg='white', command=self.show_user_score)  # Light sky blue
        self.user_score_button.pack(side=tk.LEFT, padx=10, anchor='w')  # Anchored to the left
        self.computer_score_button = tk.Button(self.frame5, text=f"Computer Score: {self.computer_score}", font=("Helvetica", 12), width=20, bg='#87CEFA', fg='white', command=self.show_computer_score)  # Light sky blue
        self.computer_score_button.pack(side=tk.LEFT, padx=10, anchor='w')  # Anchored to the left
        self.play_again_button = tk.Button(self.frame5, text="Play Again", font=("Helvetica", 12), width=15, bg='#87CEFA', fg='white', command=self.reset_game)  # Light sky blue
        self.play_again_button.pack(side=tk.LEFT, padx=10, anchor='w')  # Anchored to the left

    def set_user_choice(self, choice):
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        result = self.determine_winner(choice, computer_choice)

        self.user_choice_label.config(text=f"Your Choice: {choice}")
        self.computer_choice_label.config(text=f"Computer's Choice: {computer_choice}")
        self.result_label.config(text=result)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (
            (user_choice == "Rock" and computer_choice == "Scissors")
            or (user_choice == "Paper" and computer_choice == "Rock")
            or (user_choice == "Scissors" and computer_choice == "Paper")
        ):
            self.user_score += 1
            self.user_score_button.config(text=f"User Score: {self.user_score}")
            return "You win!"
        else:
            self.computer_score += 1
            self.computer_score_button.config(text=f"Computer Score: {self.computer_score}")
            return "You lose!"

    def show_user_score(self):
        messagebox.showinfo("User Score", f"User Score: {self.user_score}")

    def show_computer_score(self):
        messagebox.showinfo("Computer Score", f"Computer Score: {self.computer_score}")

    def reset_game(self):
        self.user_choice_label.config(text="Your Choice:")
        self.computer_choice_label.config(text="Computer's Choice:")
        self.result_label.config(text="")
        self.user_score = 0
        self.computer_score = 0
        self.user_score_button.config(text=f"User Score: {self.user_score}")
        self.computer_score_button.config(text=f"Computer Score: {self.computer_score}")


if __name__ == "__main__":
    root = tk.Tk()
    root.iconbitmap('icon.ico')
    game = RockPaperScissorsGame(root)
    root.mainloop()
