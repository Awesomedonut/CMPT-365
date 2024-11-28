from tkinter import filedialog
from PIL import Image, ImageTk

def open_image():
    file_path = filedialog.askopenfilename(
        title="Open File", 
        filetypes=[(".bmp files", "*.bmp")]
    )
    return Image.open(file_path)

def save_image(image):
    file_path = filedialog.asksaveasfilename(
        defaultextension=".bmp",
        filetypes=[
            ("png files", "*.png"),
            ("bmp files", "*.bmp")
        ]
    )
    image.save(file_path)

def update_display(image, image_label):
    if image:
        image_tk = ImageTk.PhotoImage(image)
        image_label.config(image=image_tk)
        image_label.image = image_tk  # prevent garbage collection

def display_both_imgs(image, image_label, edited_img, edited_img_label):
    update_display(image, image_label)
    if edited_img != None:
        edited_img_tk = ImageTk.PhotoImage(edited_img)
        edited_img_label.config(image=edited_img_tk)
        edited_img_label.image = edited_img_tk

def clear_display(label):
    label.config(image='')
    label.image = None