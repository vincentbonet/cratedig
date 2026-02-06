import numpy as np #
import soundfile as sf
from pathlib import Path

out_dir = Path(__file__).parent
out_dir.mkdir(exist_ok=True)

sr = 44100 # Generate a 2-second A4 tone (440 Hz)
t = np.linspace(0, 2, sr * 2, endpoint=False) 
tone = 0.1 * np.sin(2 * np.pi * 440 * t)

sf.write(out_dir / "test.wav", tone, sr)

print("Wrote examples/test.wav")
