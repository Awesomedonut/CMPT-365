from PIL import Image
import numpy as np
from grayscale import grayscale

dither_matrix = np.array([
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1]
])

dithered_img = np.zeros((4, 4), dtype=int) # init as matrix of 0s

def ordered_dithering(image):
    x_max, y_max = image.size
    image = grayscale(image)
    for x in range(0, x_max):
        for y in range(0, y_max):
            i = x % 4
            j = y % 4
            if image[x, y] > dither_matrix[i][j]:
                dithered_img(x, y) = 1
            else:
                dithered_img(x, y) = 0
