# Yan Jin Song, student number 301470175


from tkinter import *
from tkinter import filedialog, messagebox
import wave
import struct
import os

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("WAV files", "*.wav")])
    if file_path:
        try:
            display_wave_info(file_path)
            draw_waveform(file_path)
        except Exception as e:
            messagebox.showerror("Error", f"Unable to open file: {e}")

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
            sample_rate = wf.getframerate()
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

            # Plot the waveform for both channels
            plot_waveform(left_channel, 50, 'red')  # Plot left channel at y=50
            plot_waveform(right_channel, 150, 'blue')  # Plot right channel at y=150
    except Exception as e:
        messagebox.showerror("Error", f"Unable to process and draw waveform: {e}")

def plot_waveform(channel_data, y_offset, color):
    max_samples = min(65536, len(channel_data))  # Limit the number of samples to 65536
    x_scale = 1  # Horizontal scaling factor
    y_scale = 100 / max(abs(max(channel_data)), abs(min(channel_data)))  # Vertical scaling factor

    prev_x, prev_y = 0, y_offset
    for i in range(max_samples):
        x = i * x_scale
        y = y_offset - int(channel_data[i] * y_scale)

        # Draw line between previous point and current point
        waveform_canvas.create_line(prev_x, prev_y, x, y, fill=color)
        
        prev_x, prev_y = x, y

# Create the main window
window = Tk()
window.title("WAV File Reader and Waveform Display")
window.geometry("800x400")

# File selection button
browse_button = Button(window, text="Browse WAV File", command=browse_file)
browse_button.pack(pady=20)

# Labels to display wave file information
file_label = Label(window, text="File: None", font=('Arial', 12))
file_label.pack(pady=5)

channels_label = Label(window, text="Channels: -", font=('Arial', 12))
channels_label.pack(pady=5)

sample_rate_label = Label(window, text="Sampling Frequency: -", font=('Arial', 12))
sample_rate_label.pack(pady=5)

total_samples_label = Label(window, text="Number of Samples: -", font=('Arial', 12))
total_samples_label.pack(pady=5)

# Canvas for drawing the waveform
waveform_canvas = Canvas(window, width=700, height=200, bg='white')
waveform_canvas.pack(pady=20)

# Start the Tkinter event loop
window.mainloop()
