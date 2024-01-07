import tkinter as tk
import time
import threading


class DangerousWritingApp:
    def __init__(self,root):
        self.root = root
        self.root.title("Dangerous Writing App")

    
        #Variables
        self.text_content = tk.StringVar()
        self.last_update_time = time.time()

        #GUI Elements
        self.create_widgets()

        #Start monitoring for inactivity
        self.monitor_thread = threading.Thread(target=self.monitor_inactivity)
        self.monitor_thread.start()

    def create_widgets(self):
        #Text Entry
        self.text_entry = tk.Text(self.root, height=10, width=40)
        self.text_entry.pack(padx=10, pady=10)

        #start button
        self.start_button = tk.Button(self.root, text="Start Writing", command=self.start_writing)
        self.start_button(pady=10)

    def start_writing(self):
        self.text_entry.delete("1.0", tk.END) #Clear the text
        self.last_update_time = time.time() #Reset timer

    def monitor_inactivity(self):
        

