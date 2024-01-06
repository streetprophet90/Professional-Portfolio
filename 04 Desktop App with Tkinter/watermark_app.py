import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont

class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Watermark App")

        # Variables
        self.image_path = tk.StringVar()
        self.watermark_text = tk.StringVar()

        # GUI Elements
        self.create_widgets()

    

if __name__ == "__main__":
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()
