from PIL import Image
import numpy as np

def auto_level(image):
    channel_split_img = image.split()
    channels = [channel_split_img[0], channel_split_img[1], channel_split_img[2]]

    total_pixels = int(image.width * image.height)
    ideal_pixels_per_level = total_pixels/256

    vibrant_channels = []
    
    for channel in channels: # loop thru rgb
        pixel_matrix = np.array(channel) # matrix of intensity values
        pixels_per_level = np.zeros(256, dtype=int)
        
        for pixel_value in pixel_matrix.flatten():
            pixels_per_level[pixel_value] += 1
        


    img = Image.merge("RGB", vibrant_channels)
    img.save("vibrant23.jpg")

auto_level(Image.open("image3.bmp"))