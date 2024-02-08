# Password Manager

This is a simple password manager application built using Python's Tkinter library. The application allows users to generate secure passwords, save them along with associated website and email details, and retrieve them when needed.

## Features

1. **Password Generator:** The application includes a password generator that creates strong and secure passwords by combining letters (both uppercase and lowercase), numbers, and symbols.

2. **Save Passwords:** Users can input website, email, and password details into the application. The entered details are then saved to a file (`data.txt`).

3. **User Interface (UI):** The UI is created using Tkinter, providing a simple and user-friendly interface for interacting with the password manager.

## How to Use

1. **Generate Password:**
   - Click the "Generate Password" button to create a strong and secure password.
   - The generated password is displayed in the "Password" entry field and automatically copied to the clipboard.

2. **Save Password:**
   - Enter the website, email, and password details.
   - Click the "Add" button to save the entered details to the `data.txt` file.
   - A confirmation prompt will appear before saving.

## Requirements

- Python 3.x
- Tkinter library
- Pillow library (for image resizing)
- Pyperclip library

Install the required libraries using the following command:

```bash
pip install pillow pyperclip
```

## Troubleshooting

If you encounter any issues with image loading, check the following:

- Ensure the image file "logo.jpg" is in the correct location.
- Provide the full absolute path to the image file if needed.
- Confirm the image file is a valid format supported by Tkinter (e.g., JPEG, GIF, PNG).
- Resize the image using the Pillow library if it is too large.

## Contributions

Contributions are welcome! If you find any bugs, have suggestions for improvements, or want to add new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

# Code line by line, explaining each part:

```python
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
```

- `from tkinter import *`: Imports all the classes and functions from the tkinter module, which is used for creating the graphical user interface (GUI).

- `from tkinter import messagebox`: Imports the messagebox module from tkinter, which provides a way to display various types of message boxes.

- `from random import choice, randint, shuffle`: Imports specific functions from the random module. These functions will be used for generating random passwords.

- `import pyperclip`: Imports the pyperclip module, which allows the program to interact with the clipboard for copying and pasting.

```python
# Password Generator Project
def generate_password():
    # ... (code for generating a random password)
```

- Defines a function named `generate_password` that generates a random password using a combination of letters, numbers, and symbols.

```python
def save():
    # ... (code for saving website, email, and password details to a file)
```

- Defines a function named `save` that is called when the user wants to save website, email, and password details to a file (`data.txt`).

```python
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
```

- Creates a Tkinter window object, sets its title to "Password Manager," and configures padding around the window.

```python
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.jpg")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)
```

- Creates a canvas in the GUI to display an image.
- Loads the image "logo.jpg" using the PhotoImage class.
- Creates an image on the canvas using the loaded image.
- Places the canvas in the grid at row 0, column 1.

```python
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
```

- Creates Label widgets for displaying text ("Website:", "Email/Username:", "Password:").
- Places the labels in the grid at specific rows and columns.

```python
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "amoafo.alive@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)
```

- Creates Entry widgets for users to input website, email, and password details.
- Sets the width of the entry widgets.
- Places the entry widgets in the grid at specific rows and columns.
- Sets focus on the website entry.
- Inserts a default email value into the email entry.

```python
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)
```

- Creates Button widgets for generating passwords and saving details.
- Specifies the text on the buttons ("Generate Password", "Add").
- Associates the buttons with their respective functions (generate_password, save).
- Places the buttons in the grid at specific rows and columns.

```python
window.mainloop()
```

- Enters the main event loop for the Tkinter GUI, allowing the program to wait for user inputs and respond to events.

This code creates a simple password manager application with a graphical interface, password generation functionality, and the ability to save user details to a file.

# new update
# def find_password 




# Password Manager

This is a simple password manager application built using Python's Tkinter library. The application allows users to generate secure passwords, save them along with associated website and email details, retrieve them, and find saved passwords.

## Features

1. **Password Generator:** The application includes a password generator that creates strong and secure passwords by combining letters (both uppercase and lowercase), numbers, and symbols.

2. **Save Passwords:** Users can input website, email, and password details into the application. The entered details are then saved to a file (`data.txt`).

3. **Find Passwords:** Users can search for and retrieve saved passwords by entering the associated website.

4. **User Interface (UI):** The UI is created using Tkinter, providing a simple and user-friendly interface for interacting with the password manager.


```