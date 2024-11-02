from PIL import Image
import numpy as np

def count_pixels_per_level(channel):
    pixel_matrix = np.array(channel) # matrix of intensity values
    pixels_per_level = np.zeros(256, dtype=int)
    
    for pixel_value in pixel_matrix.flatten():
        pixels_per_level[pixel_value] += 1
    
    return pixel_matrix, pixels_per_level

def stretch_levels(pixels_per_level, ideal_pixels_per_level):
    stretched_levels = np.zeros(256)
    
    for level in range(256):
        if pixels_per_level[level] < ideal_pixels_per_level:
            stretched_levels[level] = level * 1.25  
        else:
            stretched_levels[level] = level * 0.85 
            
    return np.clip(stretched_levels, 0, 255)

def stretch_channel(channel, ideal_pixels_per_level):
    pixel_matrix, pixels_per_level = count_pixels_per_level(channel)
    stretched = stretch_levels(pixels_per_level, ideal_pixels_per_level)
    return Image.fromarray(stretched[pixel_matrix].astype(np.uint8))

def auto_level(image):
    channel_split_img = image.split()
    channels = [channel_split_img[0], channel_split_img[1], channel_split_img[2]]

    total_pixels = int(image.width * image.height)
    ideal_pixels_per_level = total_pixels/256
         
    vibrant_channels = [
        stretch_channel(channel, ideal_pixels_per_level) 
        for channel in channels
    ]
    
    img = Image.merge("RGB", vibrant_channels)
    img.save("vibrant28.jpg")

auto_level(Image.open("image2.bmp"))