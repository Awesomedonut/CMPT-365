# CMPT 365 Project 3 by Yan Jin Song, student number 301470175
from tkinter import *
from PIL import Image, ImageTk
from file import clear_display, open_image, save_image, update_display, display_both_imgs

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

window = Tk()
window.geometry("704x576") 
window.title("Image Viewer")

menu = Menu(window)
window.config(menu=menu)

file_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open File", command=open)
file_menu.add_command(label="Save File", command=save_file)

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