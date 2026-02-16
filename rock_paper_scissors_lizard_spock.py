import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk  # pip install pillow

# Game rules: what each choice defeats
RULES = {
    "rock": ["scissors", "lizard"],
    "paper": ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "lizard": ["spock", "paper"],
    "spock": ["scissors", "rock"]
}

CHOICES = ["rock", "paper", "scissors", "lizard", "spock"]

class RPSLSApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock–Paper–Scissors–Lizard–Spock")

        self.images = {}
        self.choice_buttons = {}
        self.selected_choice = None

        self.load_images()
        self.build_ui()

    def load_images(self):
        for name in CHOICES:
            img = Image.open(f"{name}.png")
            img = img.resize((120, 120), Image.LANCZOS)
            self.images[name] = ImageTk.PhotoImage(img)

    def build_ui(self):
        title = tk.Label(self.root, text="Rock–Paper–Scissors–Lizard–Spock",
                         font=("Helvetica", 18, "bold"))
        title.pack(pady=10)

        # Frame for selection images
        select_frame = tk.Frame(self.root)
        select_frame.pack(pady=10)

        info_label = tk.Label(self.root, text="Move the mouse and click an image to choose.",
                              font=("Helvetica", 11))
        info_label.pack(pady=5)

        for i, name in enumerate(CHOICES):
            frame = tk.Frame(select_frame, bd=2, relief="flat")
            frame.grid(row=0, column=i, padx=5)

            lbl = tk.Label(frame, image=self.images[name], cursor="hand2")
            lbl.pack()

            lbl.bind("<Enter>", lambda e, f=frame: f.config(relief="solid", bd=3))
            lbl.bind("<Leave>", lambda e, f=frame: f.config(relief="flat", bd=2))
            lbl.bind("<Button-1>", lambda e, n=name: self.on_user_choice(n))

            self.choice_buttons[name] = frame

        # Result area
        result_frame = tk.Frame(self.root)
        result_frame.pack(pady=20)

        self.user_label = tk.Label(result_frame, text="You", font=("Helvetica", 12, "bold"))
        self.user_label.grid(row=0, column=0, pady=5)

        self.comp_label = tk.Label(result_frame, text="Computer", font=("Helvetica", 12, "bold"))
        self.comp_label.grid(row=0, column=1, pady=5)

        self.user_image_label = tk.Label(result_frame)
        self.user_image_label.grid(row=1, column=0, padx=20)

        self.comp_image_label = tk.Label(result_frame)
        self.comp_image_label.grid(row=1, column=1, padx=20)

        self.result_text = tk.Label(self.root, text="", font=("Helvetica", 14, "bold"))
        self.result_text.pack(pady=10)

        reset_btn = tk.Button(self.root, text="Play Again", command=self.reset_round)
        reset_btn.pack(pady=5)

    def on_user_choice(self, choice):
        self.selected_choice = choice
        computer_choice = random.choice(CHOICES)

        # Show images side-by-side
        self.user_image_label.config(image=self.images[choice])
        self.comp_image_label.config(image=self.images[computer_choice])

        # Determine winner
        if choice == computer_choice:
            result = "It's a tie!"
        elif computer_choice in RULES[choice]:
            result = "You win!"
        else:
            result = "Computer wins!"

        self.result_text.config(text=result)

    def reset_round(self):
        self.selected_choice = None
        self.user_image_label.config(image="")
        self.comp_image_label.config(image="")
        self.result_text.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = RPSLSApp(root)
    root.mainloop()
    
