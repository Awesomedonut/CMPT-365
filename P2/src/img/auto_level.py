from PIL import Image
import numpy as np

def auto_level(image):
    channel_split_img = image.split()
    channels = [channel_split_img[0], channel_split_img[1], channel_split_img[2]]

    total_pixels = int(image.width * image.height)
    ideal_pixel_distrib = total_pixels/256

    vibrant_channel = []
    vibrant_channels = []
    
    for channel in channels: # loop thru rgb
        pixel_matrix = np.array(channel) # matrix of intensity values


        #print(pixels)


        for pixel in pixel_matrix.flat: #flatten matrix so it can be iterated over
            if pixel != ideal_pixel_distrib:
                if pixel < ideal_pixel_distrib:
                    pixel * 2
                    
                else:
                    pixel / 2
            #    print(pixel)

            vibrant_channel.append(pixel)
        vibrant_channels.append(vibrant_channel)
        img = Image.merge("RGB", Image.fromarray(vibrant_channels))
        img.save("vibrant.jpg")
        




auto_level(Image.open("image3.bmp"))