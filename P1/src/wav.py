# Yan Jin Song, student number 301470175

from tkinter import *
from tkinter import filedialog
import wave # for .wav file format
import struct  # for handling binary data

def open_file():
    path = filedialog.askopenfilename(filetypes=[(".wav files", "*.wav")])
    if path:
        get_and_display_info(path)
        display_waveforms(path)
    else:
        return

def get_and_display_info(file_path):
    with wave.open(file_path, 'rb') as waveform:  # opens in read-only mode
        sample_rate = waveform.getframerate()
        num_frames = waveform.getnframes()
        total_samples = num_frames * 2  # stereo only, i.e., 2 channels
        sample_rate_label.config(text=f"Sampling frequency: {sample_rate} Hz")
        total_samples_label.config(text=f"Total number of samples: {total_samples}")

def display_waveforms(file_path):
    with wave.open(file_path, 'rb') as waveform:
        num_frames = waveform.getnframes()
        raw_data = waveform.readframes(num_frames)
        format_string = f"<{num_frames * 2}h"  # 2 because stereo
        processed_data = struct.unpack(format_string, raw_data)

        waveform_canvas.delete("all")  # clear existing plots

        left_channel = processed_data[0::2]  # separates data for left and right, which alternates
        right_channel = processed_data[1::2]
        plot_one_waveform(left_channel, channel='left')
        plot_one_waveform(right_channel, channel='right')

def plot_one_waveform(channel_data, channel):
    canvas_width = waveform_canvas.winfo_width()
    canvas_height = waveform_canvas.winfo_height()

    max_samples = len(channel_data)  # len(channel_data) returns num of audio samples in one channel
    x_scale = canvas_width / max_samples
    max_amplitude = max(abs(max(channel_data)), abs(min(channel_data))) or 1 # range of values in waveform

    if channel == 'left':
        y_start = 0
        y_end = canvas_height / 2
    elif channel == 'right':
        y_start = canvas_height / 2
        y_end = canvas_height
    else:
        return 

    y_center = (y_start + y_end) / 2
    y_scale = (y_end - y_start) / 2 / max_amplitude

    for i in range(max_samples):
        x = int(i * x_scale)
        y = y_center - int(channel_data[i] * y_scale)
        y = max(y_start, min(y_end, y))
        waveform_canvas.create_oval(x, y, x + 1, y + 1, fill='green', outline='green')

window = Tk()
window.title("Q1: Stereo .wav file reader and waveform plotter")
window.geometry("750x580") # assuming image is no bigger than 704x576. window gives a bit of margin room so it doesn't feel to cramped

browse_button = Button(window, text="Open a .wav File", command=open_file)
browse_button.pack(pady=10)

sample_rate_label = Label(window, text="Sampling frequency: N/A", font=('Arial', 12))
sample_rate_label.pack(pady=2)
total_samples_label = Label(window, text="Total number of samples: N/A", font=('Arial', 12))
total_samples_label.pack(pady=2)

waveform_canvas = Canvas(window, bg='black')
waveform_canvas.pack(fill=BOTH, expand=True)

window.mainloop()
