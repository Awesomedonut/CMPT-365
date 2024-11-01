from PIL import Image
import numpy as np

def auto_level(image):
    channel_split_img = image.split()
    channels = [channel_split_img[0], channel_split_img[1], channel_split_img[2]]

    total_pixels = int(image.width * image.height)
    pixel_distrib = total_pixels/256

    
    for channel in channels: # loop thru rgb
        pixels = np.array(channel)

        for pixel in pixels:
            if pixel != pixel_distrib:
                print(pixel)



auto_level(Image.open("image3.bmp"))