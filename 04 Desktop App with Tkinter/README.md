# Watermark App

Automatically add watermarks to images with this desktop application, featuring a Graphical User Interface (GUI) built using Tkinter. The app allows users to upload an image and customize their watermark, whether it's a logo or text.

## Features
- **Image Selection**: Browse and select an image file from your computer.
- **Watermark Text**: Input the desired watermark text in the provided entry field.
- **Add Watermark**: Click the "Add Watermark" button to automatically apply the watermark to the selected image.

## Usage
1. Run the application.
2. Browse and select an image file.
3. Enter your watermark text.
4. Click the "Add Watermark" button.
5. View the watermarked image and save it.

## Requirements
- [Pillow](https://pypi.org/project/Pillow/): The Python Imaging Library used for image processing.
- [Tkinter](https://docs.python.org/3/library/tkinter.html): Python's standard GUI toolkit.

## Usage Example
```bash
python watermark_app.py


## Key lines of Codes explained 
### Let's go through the key lines of the code:

```python
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont
```

1. `import tkinter as tk`: Imports the Tkinter module and aliases it as `tk` for brevity.

2. `from tkinter import filedialog`: Imports the `filedialog` submodule from Tkinter, which provides a file dialog for file selection.

3. `from PIL import Image, ImageTk, ImageDraw, ImageFont`: Imports necessary classes and modules from the Pillow (PIL Fork) library for image processing.

```python
class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Watermark App")

        # Variables
        self.image_path = tk.StringVar()
        self.watermark_text = tk.StringVar()
```

4. `class WatermarkApp:`: Defines a class for the Watermark App.

5. `def __init__(self, root):`: Initializes the class with the Tkinter root window.

6. `self.root = root`: Sets the Tkinter root window as an instance variable.

7. `self.root.title("Watermark App")`: Sets the title of the Tkinter window.

8. `self.image_path = tk.StringVar()`: Creates a Tkinter StringVar to store the image path entered by the user.

9. `self.watermark_text = tk.StringVar()`: Creates a Tkinter StringVar to store the watermark text entered by the user.

```python
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
```

10. `def create_widgets(self):`: Defines a method to create GUI elements.

11. `self.label_image = tk.Label(self.root, text="Select an Image:")`: Creates a label for image selection.

12. `self.entry_image = tk.Entry(self.root, textvariable=self.image_path, width=50)`: Creates an entry widget for the image path.

13. `self.btn_browse = tk.Button(self.root, text="Browse", command=self.browse_image)`: Creates a button to browse for an image.

14. `self.label_watermark = tk.Label(self.root, text="Watermark Text:")`: Creates a label for watermark text.

15. `self.entry_watermark = tk.Entry(self.root, textvariable=self.watermark_text, width=50)`: Creates an entry widget for the watermark text.

16. `self.btn_add_watermark = tk.Button(self.root, text="Add Watermark", command=self.add_watermark)`: Creates a button to add the watermark.

```python
    def browse_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
        self.image_path.set(file_path)
```

17. `def browse_image(self):`: Defines a method to browse for an image file.

18. `file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])`: Opens a file dialog to select an image file.

19. `self.image_path.set(file_path)`: Sets the selected file path to the `image_path` variable.

```python
    def add_watermark(self):
        image_path = self.image_path.get()
        watermark_text = self.watermark_text.get()

        if image_path and watermark_text:
            original_image = Image.open(image_path)

            # Create a copy to avoid modifying the original image
            watermarked_image = original_image.copy()

            # Add watermark text
            draw = ImageDraw.Draw(watermarked_image)
            font = ImageFont.load_default()
            draw.text((10, 10), watermark_text, font=font, fill=(255, 255, 255, 128))

            # Save or display the watermarked image
            watermarked_image.save("output_watermarked.jpg")
            watermarked_image.show()
```

20. `def add_watermark(self):`: Defines a method to add a watermark to the image.

21. `image_path = self.image_path.get()`: Retrieves the image path from the `image_path` variable.

22. `watermark_text = self.watermark_text.get()`: Retrieves the watermark text from the `watermark_text` variable.

23. `original_image = Image.open(image_path)`: Opens the original image using Pillow.

24. `watermarked_image = original_image.copy()`: Creates a copy of the original image to avoid modifying it.

25. `draw = ImageDraw.Draw(watermarked_image)`: Creates a drawing object for the watermarked image.

26. `font = ImageFont.load_default()`: Loads the default font for drawing text.

27. `draw.text((10, 10), watermark_text, font=font, fill=(255, 255, 255, 128))`: Draws the watermark text on the watermarked image.

28. `watermarked_image.save("output_watermarked.jpg")`: Saves the watermarked image to a file.

29. `watermarked_image.show()`: Displays the watermarked image.