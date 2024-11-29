# CMPT 365 Project 2 by Yan Jin Song, student number 301470175

from tkinter import *
from PIL import Image, ImageTk

from file import clear_display, open_image, save_image, update_display, display_both_imgs
from img.grayscale import grayscale
from img.dithering import ordered_dithering
from img.auto_level import auto_level
from tools.magic_eraser import magic_eraser
from tools.contrast import increase_contrast



image = None
edited_img = None

def open():
    global image
    global image_label
    global edited_img_label

    clear_display(edited_img_label)
    image = open_image()
    update_display(image, image_label)

def save_file():
    global image
    global edited_img
    if edited_img != None:
        save_image(edited_img)
    else:
        save_image(image)

def edit_img(case: str):
    global image
    global edited_img
    if image == None:
        print("pls select an image")
        return

    match case:
        case "grayscale":
            edited_img = grayscale(image)
        case "dithering":
            edited_img = ordered_dithering(image)
        case "level":
            edited_img = auto_level(image)
        case "erase":
            edited_img = magic_eraser(image)
        case "contrast":
            edited_img = increase_contrast(image)

    display_both_imgs(image, image_label, edited_img, edited_img_label)


window = Tk()
window.geometry("1450x650") # the max width is 704 so in order for image 
# and processed image to be displayed side by side, the window width is slightly more than twice that
window.title("Fotoshop by Jin")

menu = Menu(window)
window.config(menu=menu)

file_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open File", command=open)
file_menu.add_command(label="Save File", command=save_file)

img_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Image Processing", menu=img_menu)
img_menu.add_command(label="Grayscale", command=lambda: edit_img("grayscale"))
img_menu.add_command(label="Ordered Dithering", command=lambda: edit_img("dithering"))
img_menu.add_command(label="Auto Level", command=lambda: edit_img("level"))
img_menu.add_command(label="Magic Eraser", command=lambda: edit_img("erase"))
img_menu.add_command(label="Increase Contrast", command=lambda: edit_img("contrast"))

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

image_label = Label(window)
image_label.pack()

frame = Frame(window)
frame.pack(side=TOP)

image_label = Label(frame)
image_label.pack(side=LEFT, padx=10)

edited_img_label = Label(frame)
edited_img_label.pack(side=LEFT, padx=10)

window.mainloop()