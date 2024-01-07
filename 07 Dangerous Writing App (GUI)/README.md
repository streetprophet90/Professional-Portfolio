# Dangerous Writing App

## Overview

The Dangerous Writing App is a desktop application designed to help writers overcome writer's block by encouraging continuous writing. Inspired by "The Most Dangerous Writing App," this app deletes all progress if the user stops writing for more than a specified duration.

## Features

- Simple and minimalistic desktop app.
- Monitors user typing activity.
- Deletes all text if there is no typing activity for a defined period (default is 5 seconds).
- Allows users to start fresh with the "Start Writing" button.

## Getting Started

To run the Dangerous Writing App, follow these steps:

1. Ensure you have Python installed on your system.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the app files.
4. Run the following command:

   ```bash
   python dangerous_writing_app.py
   ```

## How to Use

1. Launch the app by running the Python script.
2. The app window will appear with a text entry field and a "Start Writing" button.
3. Type in the text entry field to start writing.
4. If there is no typing activity for more than 5 seconds (adjustable), all text will be deleted.
5. Click the "Start Writing" button to clear the text and reset the timer.

## Adjusting Inactivity Threshold

The default inactivity threshold is set to 5 seconds. You can adjust this duration by modifying the `elapsed_time > 5` condition in the script.

```python
# Modify this line to change the inactivity threshold (in seconds)
if elapsed_time > 5:
```

## Dependencies

- Python
- Tkinter (Python's standard GUI toolkit)

## Notes

- Using threads in Tkinter requires careful consideration. This app uses a monitoring thread to detect inactivity and schedules GUI updates using the `after` method.

## License

This Dangerous Writing App is provided under the [MIT License](LICENSE).

```
Feel free to customize the README.md based on any additional details or instructions you want to provide.
```

# Every Line of Code

```python
import tkinter as tk
import threading
import time
```

1. `import tkinter as tk`: Imports the Tkinter library and aliases it as `tk` for convenience.
2. `import threading`: Imports the `threading` module for handling threads.
3. `import time`: Imports the `time` module for working with time-related functions.

```python
class DangerousWritingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dangerous Writing App")
```

4. Defines a class named `DangerousWritingApp` for the main application. The constructor (`__init__`) initializes the class instance with the root Tkinter window and sets its title.

```python
        # Variables
        self.text_content = tk.StringVar()
        self.last_update_time = time.time()
```

5. Creates two instance variables (`text_content` and `last_update_time`). `text_content` is a Tkinter `StringVar`, which is not currently used in the code. `last_update_time` is used to store the time of the last user input.

```python
        # GUI Elements
        self.create_widgets()
```

6. Calls the `create_widgets` method to set up the graphical user interface.

```python
        # Start monitoring for inactivity
        self.monitor_thread = threading.Thread(target=self.monitor_inactivity)
        self.monitor_thread.start()
```

7. Creates a new thread (`monitor_thread`) that executes the `monitor_inactivity` method in the background. This thread is started to monitor user inactivity.

```python
    def create_widgets(self):
        # Text Entry
        self.text_entry = tk.Text(self.root, height=10, width=40)
        self.text_entry.pack(padx=10, pady=10)
```

8. Creates a multiline text entry widget (`text_entry`) with a height of 10 lines and width of 40 characters. It is packed within the root window with specified padding.

```python
        # Start Button
        self.start_button = tk.Button(self.root, text="Start Writing", command=self.start_writing)
        self.start_button.pack(pady=10)
```

9. Creates a button widget (`start_button`) labeled "Start Writing" with the `start_writing` method as its command. The button is packed with a vertical padding of 10.

```python
    def start_writing(self):
        self.text_entry.delete("1.0", tk.END)  # Clear the text
        self.last_update_time = time.time()  # Reset the timer
```

10. Defines the `start_writing` method, which clears the text content in the `text_entry` widget and resets the `last_update_time` to the current time.

```python
    def monitor_inactivity(self):
        while True:
            current_time = time.time()
            elapsed_time = current_time - self.last_update_time

            if elapsed_time > 5:  # Adjust the inactivity threshold as needed (5 seconds in this example)
                self.root.after(0, self.delete_text)

            time.sleep(1)  # Check every second
```

11. Defines the `monitor_inactivity` method, which runs continuously in a loop. It calculates the elapsed time since the last user input and, if it exceeds 5 seconds, calls the `delete_text` method using `self.root.after` to schedule the deletion. It then sleeps for 1 second before checking again.

```python
    def delete_text(self):
        self.text_entry.delete("1.0", tk.END)
```

12. Defines the `delete_text` method, which deletes all the text content in the `text_entry` widget.

```python
if __name__ == "__main__":
    root = tk.Tk()
    app = DangerousWritingApp(root)
    root.mainloop()
```

13. Checks if the script is being run as the main program. If true, it creates a Tkinter root window, initializes an instance of `DangerousWritingApp`, and starts the Tkinter main event loop with `root.mainloop()`.