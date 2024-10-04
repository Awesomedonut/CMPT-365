# Yan Jin Song, student number 301470175

from tkinter import *
from tkinter import filedialog, messagebox
import wave
import struct
import os

def open_file():
    path = filedialog.askopenfilename(filetypes=[(".wav files", "*.wav")])
    if path:
            display_wave_info(path)
            draw_waveform(path)
    else:
       # return
        messagebox.showerror("invalid file path ):")

def display_wave_info(file_path):
    try:
        with wave.open(file_path, 'rb') as wf:
            num_channels = wf.getnchannels()
            sample_rate = wf.getframerate()
            num_frames = wf.getnframes()

            total_samples = num_frames * num_channels
            
            # Update the labels with the wave file information
            file_label.config(text=f"File: {os.path.basename(file_path)}")
            channels_label.config(text=f"Channels: {num_channels}")
            sample_rate_label.config(text=f"Sampling Frequency: {sample_rate} Hz")
            total_samples_label.config(text=f"Number of Samples: {total_samples}")
    except wave.Error as e:
        messagebox.showerror("Error", f"Error reading .wav file: {e}")

def draw_waveform(file_path):
    try:
        # Open the wave file and read the frames
        with wave.open(file_path, 'rb') as wf:
            num_channels = wf.getnchannels()
            num_frames = wf.getnframes()
            raw_data = wf.readframes(num_frames)

            # Unpack the PCM data
            fmt = f"<{num_frames * num_channels}h"  # Format for signed short (16-bit PCM)
            data = struct.unpack(fmt, raw_data)

            # Clear the canvas
            waveform_canvas.delete("all")

            # Extract left and right channel data
            left_channel = data[0::2]  # Left channel is at even indices
            right_channel = data[1::2]  # Right channel is at odd indices

            # Draw axes with labels
            draw_axes()

            # Plot the waveform for both channels using dots
            plot_waveform(left_channel, 50, 'red')  # Plot left channel at y=50
            plot_waveform(right_channel, 150, 'blue')  # Plot right channel at y=150
    except Exception as e:
        messagebox.showerror("Error", f"Unable to process and draw waveform: {e}")

def draw_axes():
    # Draw x-axis
    waveform_canvas.create_line(50, 100, 650, 100, fill="black")
    waveform_canvas.create_text(660, 100, text="Time", anchor=W)


    # Adjust the text position slightly to make it visible
    # waveform_canvas.create_text(660, 105, text="Time", anchor=W)  # Slightly lower on the y-axis
    # waveform_canvas.create_text(45, 10, text="Amplitude", anchor=E)  # Left side is okay

    # Draw y-axis
    waveform_canvas.create_line(50, 10, 50, 190, fill="black")
    waveform_canvas.create_text(40, 10, text="Amplitude", anchor=E)

    # Add some ticks and labels on the axes
    for i in range(0, 601, 100):  # x-axis ticks
        waveform_canvas.create_line(50 + i, 95, 50 + i, 105, fill="black")
        waveform_canvas.create_text(50 + i, 110, text=f"{i}", anchor=N)

    for i in range(50, 151, 50):  # y-axis ticks
        waveform_canvas.create_line(45, i, 55, i, fill="black")
        waveform_canvas.create_text(40, i, text=f"{100 - i}", anchor=E)

def plot_waveform(channel_data, y_offset, color):
    max_samples = min(65536, len(channel_data))  # Limit the number of samples to 65536
    x_scale = 600 / max_samples  # Horizontal scaling factor
    y_scale = 100 / max(abs(max(channel_data)), abs(min(channel_data)))  # Vertical scaling factor

    # Plot points for each sample to get the jagged look
    for i in range(max_samples):
        x = 50 + int(i * x_scale)  # Offset by 50 for the y-axis
        y = y_offset - int(channel_data[i] * y_scale)  # Offset by y_offset for channels

        # Draw a small dot (oval with the same width and height to appear like a dot)
        waveform_canvas.create_oval(x, y, x + 2, y + 2, fill=color, outline=color)


window = Tk()
window.title("WAV File Reader and Waveform Display")
window.geometry("800x600")

browse_button = Button(window, text="Open a .wav File", command=open_file)
browse_button.pack(pady=20)

file_label = Label(window, text="File: None", font=('Arial', 12))
file_label.pack(pady=5)
channels_label = Label(window, text="Channels: -", font=('Arial', 12))
channels_label.pack(pady=5)
sample_rate_label = Label(window, text="Sampling Frequency: -", font=('Arial', 12))
sample_rate_label.pack(pady=5)
total_samples_label = Label(window, text="Number of Samples: -", font=('Arial', 12))
total_samples_label.pack(pady=5)

waveform_canvas = Canvas(window, width=700, height=400, bg='white')
waveform_canvas.pack(pady=20, side=TOP, anchor=CENTER)


window.mainloop()