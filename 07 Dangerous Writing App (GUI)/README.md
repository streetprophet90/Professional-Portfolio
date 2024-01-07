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