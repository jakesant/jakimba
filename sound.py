import numpy as np
import pyaudio

def generate_sine_wave(frequency, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)
    return wave

def play_wave(wave, sample_rate):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=sample_rate,
                    output=True)
    stream.write(wave.astype(np.float32).tostring())
    stream.stop_stream()
    stream.close()
    p.terminate()
