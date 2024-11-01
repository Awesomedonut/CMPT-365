# CMPT 365 Project 2 by Yan Jin Song, student number 301470175

from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

def open_file():
    file_path = filedialog.askopenfilename(
        title="Open File", 
        filetypes=[(".bmp files", "*.bmp")]
    )
    
    if file_path:
            image = Image.open(file_path)
            image_tk = ImageTk.PhotoImage(image) # converting image to a format that tkinter can use
            image_label.config(image=image_tk) # widget so image_tk can be displayed in tkinter
            image_label.image = image_tk # prevents python garbage collector from removing image
    else:
        return

def exit():
    window.quit()

window = Tk()
window.geometry("900x650")
window.title("Fotoshop by Jin")

menu = Menu(window)
window.config(menu=menu)

file_menu = Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open File", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit)

image_label = Label(window)
image_label.pack()

window.mainloop()