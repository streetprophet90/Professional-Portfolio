# Color Extractor

Color Extractor is a web application built with Flask that allows users to upload an image and discover the top 10 most common colors in that image.

## Features

- Upload an image to extract colors.
- Display the top 10 most common colors with their HEX codes.

## Prerequisites

- Python 3.x
- Flask
- numpy
- opencv-python

Install the required dependencies using:

```bash
pip install Flask numpy opencv-python
```

## Usage

1. Clone the repository:

```bash
git clone https://github.com/streetprophet90/color-extractor.git
cd color-extractor
```

2. Run the Flask application:

```bash
python app.py
```

3. Open your browser and visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

4. Upload an image and view the top 10 most common colors.

## Project Structure

- **app.py**: Main Flask application file.
- **templates**: Folder containing HTML templates.
  - **index.html**: Main page template for uploading images.
  - **result.html**: Template for displaying color extraction results.
- **static**: Folder to store uploaded images.

## License
```
This Color Extractor application is provided under the [MIT License](LICENSE).
```



# file's code and explain the purpose of each line:

### `app.py` (Flask application):

```python
from flask import Flask, render_template, request
import cv2
import numpy as np
from collections import Counter
import webcolors
```

1. **Import Flask and necessary libraries:**
   - `Flask`: Imports the Flask web framework.
   - `render_template`: Function to render HTML templates.
   - `request`: Handles HTTP requests in Flask.
   - `cv2`: OpenCV library for image processing.
   - `numpy as np`: NumPy for numerical operations.
   - `Counter`: Part of Python's collections module, used for counting hashable objects.
   - `webcolors`: Library for working with color names and RGB values.

```python
app = Flask(__name__)
```

2. **Create a Flask application:**
   - Initializes a Flask web application.

```python
def get_top_colors(image_path, num_colors=10):
    # Function to get the top colors from an image
```

3. **Function to extract top colors:**
   - `get_top_colors` is a function that takes an image path and returns the top colors as a list of tuples.

```python
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
```

4. **Read and convert image:**
   - Reads the image using OpenCV and converts it from BGR to RGB color space.

```python
    pixels = image.reshape((-1, 3))
```

5. **Reshape image pixels:**
   - Reshapes the image to be a list of pixels.

```python
    counter = Counter(map(tuple, pixels))
    most_common = counter.most_common(num_colors)
```

6. **Count most common colors:**
   - Uses a Counter to count the occurrences of each unique color.
   - Finds the most common colors using `most_common` method.

```python
    top_colors = [(webcolors.rgb_to_hex(color), count) for color, count in most_common]
```

7. **Convert RGB to web colors:**
   - Converts RGB color values to web colors using `webcolors.rgb_to_hex`.

```python
    return top_colors
```

8. **Return top colors:**
   - Returns the list of top colors.

```python
@app.route('/', methods=['GET', 'POST'])
def index():
    # Flask route for the main page
```

9. **Flask route for the main page:**
   - Defines a Flask route for the main page that handles both GET and POST requests.

```python
    if request.method == 'POST':
        # Check if a file was uploaded using POST request
```

10. **Check if file was uploaded:**
    - Checks if the request method is POST, indicating that a form was submitted.

```python
        file = request.files['file']
        if file:
            image_path = "static/uploaded_image.jpg"
            file.save(image_path)
```

11. **Handle file upload:**
    - Retrieves the uploaded file from the request.
    - Saves the uploaded image to a static folder.

```python
            top_colors = get_top_colors(image_path)
            return render_template('result.html', image_path=image_path, top_colors=top_colors)
```

12. **Extract top colors and render results:**
    - Calls the `get_top_colors` function to extract top colors from the uploaded image.
    - Renders the `result.html` template with the image path and top colors as parameters.

```python
    return render_template('index.html')
```

13. **Render main page template:**
    - Renders the `index.html` template for the main page when the request method is GET.

```python
if __name__ == '__main__':
    app.run(debug=True)
```

14. **Run the Flask application:**
    - Checks if the script is being run as the main program.
    - Runs the Flask application with debugging enabled if true.

### `templates/index.html` (HTML template for the main page):

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Color Extractor</title>
</head>
<body>
    <h1>Color Extractor</h1>
    <form method="post" enctype="multipart/form-data">
        <label for="file">Upload Image:</label>
        <input type="file" name="file" accept="image/*" required>
        <br>
        <button type="submit">Extract Colors</button>
    </form>
</body>
</html>
```

1. **HTML template for the main page:**
   - Displays a simple form with a file input for image upload.

### `templates/result.html` (HTML template for displaying results):

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Color Extractor - Results</title>
</head>
<body>
    <h1>Color Extractor - Results</h1>
    
    <img src="{{ image_path }}" alt="Uploaded Image" width="300">

    <h