from PIL import Image
import numpy as np

def magic_eraser(image):
    image = image.convert("RGBA")
    img_array = np.array(image)
    x_max, y_max = img_array[:, :, 0].shape
    bg = img_array[0, 0][:3].astype(int)
    erase_range = 60
    
    for y in range(y_max):
        for x in range(x_max):
            pixel = img_array[x, y].astype(int)
            r, g, b, a = pixel
            if (abs(int(r) - bg[0]) < erase_range and 
                abs(int(g) - bg[1]) < erase_range and 
                abs(int(b) - bg[2]) < erase_range):
                img_array[x, y] = (r, g, b, 0)
    
    return Image.fromarray(img_array)

