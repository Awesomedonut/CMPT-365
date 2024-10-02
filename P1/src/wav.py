import tkinter as tk
from tkinter import filedialog, messagebox
import wave
import os

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("WAV files", "*.wav")])
    if file_path:
        try:
            display_wave_info(file_path)
        except Exception as e:
            messagebox.showerror("Error", f"Unable to open file: {e}")

def display_wave_info(file_path):
    try:
        with wave.open(file_path, 'rb') as wf:
            num_channels = wf.getnchannels()
            sample_width = wf.getsampwidth()
            sample_rate = wf.getframerate()
            num_frames = wf.getnframes()

            total_samples = num_frames * num_channels
            
            file_label.config(text=f"File: {os.path.basename(file_path)}")
            sample_rate_label.config(text=f"Sampling Frequency: {sample_rate} Hz")
            total_samples_label.config(text=f"Number of Samples: {total_samples}")
    except wave.Error as e:
        messagebox.showerror("Error", f"Error reading .wav file: {e}")

root = tk.Tk()
root.title("WAV File Reader")
root.geometry("400x300")

browse_button = tk.Button(root, text="Browse WAV File", command=browse_file)
browse_button.pack(pady=20)

file_label = tk.Label(root, text="File: None", font=('Arial', 12))
file_label.pack(pady=5)

sample_rate_label = tk.Label(root, text="Sampling Frequency: -", font=('Arial', 12))
sample_rate_label.pack(pady=5)

total_samples_label = tk.Label(root, text="Number of Samples: -", font=('Arial', 12))
total_samples_label.pack(pady=5)

root.mainloop()
