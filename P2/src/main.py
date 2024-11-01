# CMPT 365 Project 2 by Yan Jin Song, student number 301470175

from tkinter import *
from PIL import Image

from file import open_image, save_image, update_display
from img.grayscale import grayscale_image
from img.dithering import ordered_dithering
from img.auto_level import auto_level_image
from tools.magic_eraser import magic_eraser
from tools.drawing import draw_with_pen, erase
from tools.crop import crop_image
from text import add_text_to_image



window = Tk()
window.geometry("900x650")
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
img_menu.add_command(label="Ordered Dithering", command=dithering)
img_menu.add_command(label="Auto Level", command=auto_level)

tools_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Optional Tools", menu=tools_menu)
tools_menu.add_command(label="Magic Eraser", command=magic_eraser)
tools_menu.add_command(label="Pen", command=pen)
tools_menu.add_command(label="Eraser", command=eraser)
tools_menu.add_command(label="Crop", command=crop)
tools_menu.add_command(label="Add Text", command=text)

menu.add_separator()
menu.add_command(label="Exit", command=window.quit)

image_label = Label(window)
image_label.pack()

window.mainloop()