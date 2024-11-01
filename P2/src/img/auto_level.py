from PIL import Image, ImageEnhance

def auto_level(image):
    channel_split_img = image.split()
    channels = [3]
    channels[0] = channel_split_img[0]
    channels[1] = channel_split_img[1]
    channels[2] = channel_split_img[2]
