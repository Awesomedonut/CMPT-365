from PIL import Image

def grayscale(image):
    channel_split_img = image.split()
    r_channel, g_channel, b_channel = channel_split_img[0], channel_split_img[1], channel_split_img[2]
    y_channel: list[int] = []
    
    for r_pixel, g_pixel, b_pixel in zip(r_channel.getdata(), g_channel.getdata(), b_channel.getdata()):
        luminance: int = (r_pixel * 0.299) + (g_pixel * 0.587) + (b_pixel * 0.114)
        luminance = int(luminance)
        y_channel.append((luminance, luminance, luminance))
        #  print(luminance)
    
    gray_img = image.copy()
    gray_img.putdata(y_channel)
    return gray_img

# grayscale("image3.bmp")

# x, y, z = [1,2,3], [4,5,6], [7,8,9]