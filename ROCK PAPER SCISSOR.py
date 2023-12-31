import tkinter as tk
import random

def play_game(user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    comp_choice = random.choice(choices)
    
    if user_choice == comp_choice:
        result_label.config(text=f"Computer chose {comp_choice}. It's a tie!")
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
         (user_choice == "Paper" and comp_choice == "Rock") or \
         (user_choice == "Scissors" and comp_choice == "Paper"):
        result_label.config(text=f"Computer chose {comp_choice}. You win!")
    else:
        result_label.config(text=f"Computer chose {comp_choice}. Computer wins!")

root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

def create_button(choice):
    return tk.Button(root, text=choice, width=10, command=lambda: play_game(choice))

rock_button = create_button("Rock")
paper_button = create_button("Paper")
scissors_button = create_button("Scissors")

rock_button.grid(row=0, column=0, padx=10, pady=5)
paper_button.grid(row=0, column=1, padx=10, pady=5)
scissors_button.grid(row=0, column=2, padx=10, pady=5)

result_label = tk.Label(root, text="Make your choice!", font=("Arial", 12))
result_label.grid(row=1, columnspan=3, padx=10, pady=10)

root.mainloop()
