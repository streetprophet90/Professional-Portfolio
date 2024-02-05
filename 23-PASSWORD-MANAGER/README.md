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