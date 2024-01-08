from flask import Flask, render_template, request
import cv2
import numpy as np
from collections import Counter
import webcolors

app = Flask(__name__)

def get_top_colors(image_path, num_colors=10):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Reshape the image to be a list of pixels
    pixels = image.reshape((-1, 3))

    # Find the most common colors
    counter = Counter(map(tuple, pixels))
    most_common = counter.most_common(num_colors)

    # Convert RGB to web colors
    top_colors = [(webcolors.rgb_to_hex(color), count) for color, count in most_common]

    return top_colors