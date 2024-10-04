# Yan Jin Song, student number 301470175

from tkinter import *
from tkinter import filedialog, messagebox
import wave
import struct # for handling binary data
import os # for file paths

def open_file():
    path = filedialog.askopenfilename(filetypes=[(".wav files", "*.wav")])
    if path:
        get_and_display_info(path)
        display_waveforms(path)
    else:
        return

def get_and_display_info(file_path):
    with wave.open(file_path, 'rb') as waveform: # opens in read only mode
        sample_rate = waveform.getframerate()
        num_frames = waveform.getnframes()
        total_samples = num_frames * 2  # stereo only, aka 2 channels
        file_label.config(text=f"File: {os.path.basename(file_path)}")
        sample_rate_label.config(text=f"Sampling frequency: {sample_rate} Hz")
        total_samples_label.config(text=f"Total number of samples: {total_samples}")

def display_waveforms(file_path):
    with wave.open(file_path, 'rb') as waveform:
        num_frames = waveform.getnframes()
        raw_data = waveform.readframes(num_frames)
        format_string = f"<{num_frames * 2}h"  # 2 because stereo. how to interpret binary data
        data = struct.unpack(format_string, raw_data)

        waveform_canvas.delete("all") # clear existing plots

        left_channel = data[0::2] # separates data for left and right, which alternates
        right_channel = data[1::2]
        plot_one_waveform(left_channel, channel='left')
        plot_one_waveform(right_channel, channel='right')

def plot_one_waveform(channel_data, channel):
    max_samples = min(131072, len(channel_data))  # Limit for performance
    x_scale = PLOT_WIDTH / max_samples

    # Compute max amplitude for scaling
    max_amplitude = max(abs(max(channel_data)), abs(min(channel_data))) or 1

    # Assign vertical space for each channel
    if channel == 'left':
        y_start = PLOT_Y_START
        y_end = PLOT_Y_START + PLOT_HEIGHT / 2
    elif channel == 'right':
        y_start = PLOT_Y_START + PLOT_HEIGHT / 2
        y_end = PLOT_Y_END
    else:
        return  # Invalid channel

    y_center = (y_start + y_end) / 2
    y_scale = (y_end - y_start) / 2 / max_amplitude  # Scale to fit in half the canvas height

    for i in range(max_samples):
        x = PLOT_X_START + int(i * x_scale)
        y = y_center - int(channel_data[i] * y_scale)
        y = max(y_start, min(y_end, y))  # Ensure y is within the channel's area
        waveform_canvas.create_oval(x, y, x + 1, y + 1, fill='green', outline='green')

def setup_plot_dimensions():
    global PLOT_X_START, PLOT_X_END, PLOT_WIDTH, PLOT_Y_START, PLOT_Y_END, PLOT_HEIGHT
    waveform_canvas.update_idletasks()
    canvas_width = waveform_canvas.winfo_width()
    canvas_height = waveform_canvas.winfo_height()
    PLOT_X_START = 0
    PLOT_X_END = canvas_width
    PLOT_WIDTH = PLOT_X_END - PLOT_X_START
    PLOT_Y_START = 0
    PLOT_Y_END = canvas_height
    PLOT_HEIGHT = PLOT_Y_END - PLOT_Y_START

window = Tk()
window.title("Q1: Stero .wav file reader and waveform plotter")
window.geometry("800x600")

browse_button = Button(window, text="Open a .wav File", command=open_file)
browse_button.pack(pady=10)

file_label = Label(window, text="File: None", font=('Arial', 12))
file_label.pack(pady=2)
sample_rate_label = Label(window, text="Sampling frequency: N/A", font=('Arial', 12))
sample_rate_label.pack(pady=2)
total_samples_label = Label(window, text="Total number of samples: N/A", font=('Arial', 12))
total_samples_label.pack(pady=2)

waveform_canvas = Canvas(window, bg='black')
waveform_canvas.pack(fill=BOTH, expand=True)

# Set up plot dimensions after the window has been rendered
window.update_idletasks()
setup_plot_dimensions()

window.mainloop()
