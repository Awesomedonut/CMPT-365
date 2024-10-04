# Yan Jin Song, student number 301470175

from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

def open_bmp_image():
    file_path = filedialog.askopenfilename(
        title="Open File", 
        filetypes=[(".bmp files", "*.bmp")]
    )
    
    if file_path:
        try:
            img = Image.open(file_path)


            # Display the image
            img_tk = ImageTk.PhotoImage(img)
            image_label.config(image=img_tk)
            image_label.image = img_tk

        except IOError:
            messagebox.showerror("Error", "File could not be opened or is not a valid BMP image.")

def exit_program():
    window.quit()

# Main window setup
window = Tk()
window.geometry("800x600")
window.title("Q2:.bmp file displayer")

# Creating a menu bar
menu_bar = Menu(window)
window.config(menu=menu_bar)

# Adding "File" menu
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open File", command=open_bmp_image)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_program)

# Display area for image
image_label = Label(window)
image_label.pack()

# Info label for image details
info_label = Label(window, text="Image info will be displayed here.")
info_label.pack(pady=10)

# Start the main loop
window.mainloop()
