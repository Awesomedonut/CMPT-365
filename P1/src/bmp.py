import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

# Function to open and display a BMP image
def open_bmp_image():
    # Open a file dialog to select the image file
    file_path = filedialog.askopenfilename(
        title="Select a BMP File", 
        filetypes=[("BMP files", "*.bmp")]
    )
    
    if file_path:
        try:
            # Open and load the image
            img = Image.open(file_path)
            img.thumbnail((400, 400))  # Resize for display purposes

            # Convert the image for tkinter display
            img_tk = ImageTk.PhotoImage(img)

            # Update the label with the image
            image_label.config(image=img_tk)
            image_label.image = img_tk  # Keep a reference to avoid garbage collection

            # Display image info
            info_label.config(text=f"Image size: {img.size}, Image mode: {img.mode}")
        except IOError:
            messagebox.showerror("Error", "File could not be opened or is not a valid BMP image.")

# Set up the main application window
root = tk.Tk()
root.title("BMP Image Viewer")

# Create a button to open BMP files
open_button = tk.Button(root, text="Open BMP File", command=open_bmp_image)
open_button.pack(pady=10)

# Label to display the image
image_label = tk.Label(root)
image_label.pack()

# Label to display image info
info_label = tk.Label(root, text="Image info will be displayed here.")
info_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
