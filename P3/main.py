# CMPT 365 Project 3 by Yan Jin Song, student number 301470175
from tkinter import *
#from PIL import Image, ImageTk
from file import clear_display, open_image, save_image, update_display, get_image_data
from huffman import huffman_encode
from jpeg_lossless import lossless_jpeg_compress

image = None
compression_info = None

def open():
    global image
    global image_label
    global compression_info

    image = open_image()
    if image:
        update_display(image, image_label)
        compress_image()

def calc_compression_ratio(image_data, width, height):
    original_bits = width * height * 24  # each pixel has 24 bits RGB
    
    
    huffman_codes, huff_coded_arr = huffman_encode(image_data)
    #print(huffman_codes)
    huffman_compressed_bits = len(huff_coded_arr)
    huffman_ratio = original_bits / huffman_compressed_bits
    
   
   
    lossless_jpeg_compressed = lossless_jpeg_compress(image_data, width, height)
    total_compressed_bits = sum(lossless_jpeg_compressed['compressed_sizes'])
    lossless_jpeg_ratio = original_bits / total_compressed_bits
    
    return huffman_ratio, lossless_jpeg_ratio



def compress_image():
    global image
    global compression_info
    
    if image:
        width, height = image.size
        image_data = get_image_data(image)
        
        ratios = calc_compression_ratio(image_data, width, height)
        
        compression_text = (
            f"(1) huffman only:\n"
            f"compression ratio: {ratios[0]:.2f}\n\n"

            f"(2) lossless jpeg mode + huffman:\n"
            f"compression ratio: {ratios[1]:.2f}\n"
    
        )
        compression_label.config(text=compression_text)

def save_file():
    global image
    if image:
        save_image(image)

window = Tk()
window.geometry("1000x650")
window.title("Project 3")

menu = Menu(window)
window.config(menu=menu)

file_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open File", command=open)
file_menu.add_command(label="Save File", command=save_file)

exit_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Exit", menu=exit_menu)
exit_menu.add_command(label="Exit", command=window.quit)


left_frame = Frame(window)
left_frame.pack(side=LEFT, padx=20)

image_label = Label(left_frame)
image_label.pack()


right_frame = Frame(window)
right_frame.pack(side=LEFT, padx=20)

compression_label = Label(right_frame, 
                         text="compression ratios:\n pls open an image:",
                         justify=LEFT,
                         font=('Courier', 12))
compression_label.pack(pady=20)

window.mainloop()