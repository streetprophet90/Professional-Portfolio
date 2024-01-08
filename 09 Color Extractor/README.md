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

This Color Extractor application is provided under the [MIT License](LICENSE).
```

Please customize the README.md based on any additional details or instructions you want to provide.