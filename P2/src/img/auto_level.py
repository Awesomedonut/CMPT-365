from PIL import Image
import numpy as np

def auto_level(image):
    channel_split_img = image.split()
    channels = [channel_split_img[0], channel_split_img[1], channel_split_img[2]]

    total_pixels = image.width * image.height

    
    for channel in channels: # loop thru rgb
        pixels = np.array(channel)

        for pixel in pixels:
            if pixel != total_pixels/256:
                print(pixel)



auto_level(Image.open("image3.bmp"))