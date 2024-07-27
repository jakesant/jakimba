import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from sound import generate_sine_wave, play_wave
from adsr import apply_adsr_envelope

class ADSRGui:
    def __init__(self, root):
        self.root = root
        self.root.title("ADSR Sine Wave Generator")

        self.freq = tk.DoubleVar(value=440.0)
        self.attack = tk.DoubleVar(value=0.1)
        self.decay = tk.DoubleVar(value=0.1)
        self.sustain = tk.DoubleVar(value=0.7)
        self.release = tk.DoubleVar(value=0.1)
        self.sample_rate = 44100
        self.duration = 2.0

        self.create_widgets()
        self.plot_waveform()

    def create_widgets(self):
        tk.Label(self.root, text="Frequency (Hz)").pack()
        tk.Scale(self.root, variable=self.freq, from_=20, to_=2000, resolution=1, orient="horizontal").pack()

        tk.Label(self.root, text="Attack Time (s)").pack()
        tk.Scale(self.root, variable=self.attack, from_=0, to_=1, resolution=0.01, orient="horizontal").pack()

        tk.Label(self.root, text="Decay Time (s)").pack()
        tk.Scale(self.root, variable=self.decay, from_=0, to_=1, resolution=0.01, orient="horizontal").pack()

        tk.Label(self.root, text="Sustain Level").pack()
        tk.Scale(self.root, variable=self.sustain, from_=0, to_=1, resolution=0.01, orient="horizontal").pack()

        tk.Label(self.root, text="Release Time (s)").pack()
        tk.Scale(self.root, variable=self.release, from_=0, to_=1, resolution=0.01, orient="horizontal").pack()

        tk.Button(self.root, text="Play", command=self.play).pack()

    def generate_waveform(self):
        wave = generate_sine_wave(self.freq.get(), self.duration, self.sample_rate)
        wave = apply_adsr_envelope(wave, self.sample_rate, self.attack.get(), self.decay.get(), self.sustain.get(), self.release.get())
        return wave

    def plot_waveform(self):
        wave = self.generate_waveform()
        fig, ax = plt.subplots(figsize=(5, 2))
        ax.plot(wave[:1000])  # Plot the first 1000 samples
        ax.set_xlabel("Sample")
        ax.set_ylabel("Amplitude")

        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().pack()
        canvas.get_tk_widget().pack_forget()  # Prevents multiple plots stacking

    def play(self):
        wave = self.generate_waveform()
        play_wave(wave, self.sample_rate)
        self.plot_waveform()
