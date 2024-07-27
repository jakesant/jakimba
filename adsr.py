import numpy as np

def apply_adsr_envelope(wave, sample_rate, attack_time, decay_time, sustain_level, release_time):
    total_samples = len(wave)
    attack_samples = int(attack_time * sample_rate)
    decay_samples = int(decay_time * sample_rate)
    release_samples = int(release_time * sample_rate)
    sustain_samples = total_samples - attack_samples - decay_samples - release_samples

    if sustain_samples < 0:
        raise ValueError("ADSR times exceed wave duration.")

    envelope = np.concatenate([
        np.linspace(0, 1, attack_samples),  # Attack
        np.linspace(1, sustain_level, decay_samples),  # Decay
        np.full(sustain_samples, sustain_level),  # Sustain
        np.linspace(sustain_level, 0, release_samples)  # Release
    ])

    return wave * envelope
