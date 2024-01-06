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

    def create_widgets(self):
        # Image Selection
        self.label_image = tk.Label(self.root, text="Select an Image:")
        self.label_image.grid(row=0, column=0, padx=10, pady=10)

        self.entry_image = tk.Entry(self.root, textvariable=self.image_path, width=50)
        self.entry_image.grid(row=0, column=1, padx=10, pady=10)

        self.btn_browse = tk.Button(self.root, text="Browse", command=self.browse_image)
        self.btn_browse.grid(row=0, column=2, padx=10, pady=10)

        # Watermark Text
        self.label_watermark = tk.Label(self.root, text="Watermark Text:")
        self.label_watermark.grid(row=1, column=0, padx=10, pady=10)

        self.entry_watermark = tk.Entry(self.root, textvariable=self.watermark_text, width=50)
        self.entry_watermark.grid(row=1, column=1, padx=10, pady=10)

        # Add Watermark Button
        self.btn_add_watermark = tk.Button(self.root, text="Add Watermark", command=self.add_watermark)
        self.btn_add_watermark.grid(row=2, column=1, pady=20)
    

if __name__ == "__main__":
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()
