import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

def open_bmp_image():
    file_path = filedialog.askopenfilename(
        title="Select a BMP File", 
        filetypes=[("BMP files", "*.bmp")]
    )
    
    if file_path:
        try:
            img = Image.open(file_path)
            img.thumbnail((400, 400))  
            img_tk = ImageTk.PhotoImage(img)
            image_label.config(image=img_tk)
            image_label.image = img_tk  

            info_label.config(text=f"Image size: {img.size}, Image mode: {img.mode}")
        except IOError:
            messagebox.showerror("Error", "File could not be opened or is not a valid BMP image.")

root = tk.Tk()
root.title("BMP Image Viewer")

open_button = tk.Button(root, text="Open BMP File", command=open_bmp_image)
open_button.pack(pady=10)

image_label = tk.Label(root)
image_label.pack()

root.mainloop()
