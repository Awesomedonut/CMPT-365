from PIL import Image
import numpy as np

def auto_level(image):
    channel_split_img = image.split()
    channels = [channel_split_img[0], channel_split_img[1], channel_split_img[2]]

    total_pixels = int(image.width * image.height)
    ideal_pixel_distrib = total_pixels/256

    vibrant_channels = []
    
    for channel in channels: # loop thru rgb
        pixel_matrix = np.array(channel) # matrix of intensity values
        vibrant_channel = np.zeros_like(pixel_matrix)

        for i, pixel in np.ndenumerate(pixel_matrix):
            if pixel != ideal_pixel_distrib:
                if pixel < ideal_pixel_distrib:
                    vibrant_channel[i] = min(255, pixel * 2)
                else:
                    vibrant_channel[i] = max(0, pixel / 2)

        vibrant_channels.append(Image.fromarray(vibrant_channel.astype(np.uint8)))

    img = Image.merge("RGB", vibrant_channels)
    img.save("vibrant.jpg")

auto_level(Image.open("image3.bmp"))