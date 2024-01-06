import tkinter as tk
from time import time

class TypingSpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")

        # Variables
        self.sample_text = "The quick brown fox jumps over the lazy dog."
        self.user_input = tk.StringVar()
        self.start_time = None

        # GUI Elements
        self.create_widgets()

    def create_widgets(self):
        # Display Sample Text
        self.label_sample_text = tk.Label(self.root, text=self.sample_text, wraplength=400)
        self.label_sample_text.grid(row=0, column=0, columnspan=2, pady=10)

        # User Input Entry
        self.entry_user_input = tk.Entry(self.root, textvariable=self.user_input, width=50)
        self.entry_user_input.grid(row=1, column=0, columnspan=2, pady=10)

        # Start Button
        self.btn_start = tk.Button(self.root, text="Start Typing", command=self.start_typing)
        self.btn_start.grid(row=2, column=0, pady=10)

        # Calculate WPM Button
        self.btn_calculate_wpm = tk.Button(self.root, text="Calculate WPM", command=self.calculate_wpm)
        self.btn_calculate_wpm.grid(row=2, column=1, pady=10)

        # Typing Speed Label
        self.label_typing_speed = tk.Label(self.root, text="Typing Speed: ")
        self.label_typing_speed.grid(row=3, column=0, columnspan=2, pady=10)



    

