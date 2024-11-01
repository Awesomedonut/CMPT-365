# CMPT 365 Project 2 by Yan Jin Song, student number 301470175

from tkinter import *
from PIL import Image

from file import open_image, save_image, update_display
from img.grayscale import grayscale
from img.dithering import ordered_dithering
from img.auto_level import auto_level_image
from tools.magic_eraser import magic_eraser


from test import test

image = None

# def open_file():
#     global image
#     image = open_image()
#     update_display(image, )

# def save_file():
#     global image
#     save_image(image)

def edit_img(case: str):
    global image
    if image == None:
        print("pls select an image")
        
    match case:
        case "grayscale":
            grayscale(image)

    update_display()

    


window = Tk()
window.geometry("1500x650") # the max width is 704 so in order for image 
# and processed image to be displayed side by side, the window width is slightly more than twice that
window.title("Fotoshop by Jin")

menu = Menu(window)
window.config(menu=menu)

file_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open File", command=open_file)
file_menu.add_command(label="Save File", command=save_file)

img_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Image Processing", menu=img_menu)
img_menu.add_command(label="Grayscale", command=grayscale)
# img_menu.add_command(label="Ordered Dithering", command=dithering)
# img_menu.add_command(label="Auto Level", command=auto_level)

# tools_menu = Menu(menu, tearoff=0)
# menu.add_cascade(label="Optional Tools", menu=tools_menu)
# tools_menu.add_command(label="Magic Eraser", command=lambda: test("asdffjsdf"))
# tools_menu.add_command(label="Pen", command=pen)
# tools_menu.add_command(label="Eraser", command=eraser)
# tools_menu.add_command(label="Crop", command=crop)
# tools_menu.add_command(label="Add Text", command=text)

exit_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Exit", menu=exit_menu)
exit_menu.add_command(label="Exit", command=window.quit)

window.mainloop()