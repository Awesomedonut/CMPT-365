from PIL import Image
import numpy as np
from grayscale import grayscale

dither_matrix = np.array([
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1]
]) * (255/16) 

def ordered_dithering(image):
    image = grayscale(image)
    img_array = np.array(image)
    y_max, x_max = img_array.shape
    dithered_img = np.zeros((y_max, x_max), dtype=np.uint8) # init as matrix of 0s
    
    for y in range(y_max):
        for x in range(x_max):
            i = y % 4
            j = x % 4
            if float(img_array[y, x]) > float(dither_matrix[i, j]):

                dithered_img[y, x] = 255

    return Image.fromarray(dithered_img)

result = ordered_dithering(Image.open("image3.bmp"))
result.save("dithered_output.bmp")

