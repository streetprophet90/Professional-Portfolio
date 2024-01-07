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

        