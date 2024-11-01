from PIL import Image



def grayscale(image):
    img = Image.open(image)
    img = img.split()
    r_channel, g_channel, b_channel = img[0], img[1], img[2]
    
    for r_pixel, g_pixel, b_pixel in r_channel.getdata(), g_channel.getdata(), b_channel.getdata():
        luminance = (r_pixel * 0.299) + (g_pixel * 0.587) + (b_pixel * 0.114)
        print(luminance)
       # print(r_pixel)

        # for j in range(0, 165):
        #     print(r[i][j])



grayscale("image3.bmp")