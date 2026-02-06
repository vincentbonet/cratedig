from pathlib import Path
from crate.features import detect_bpm
import soundfile as sf

AUDIO_EXTS = {".wav", ".aiff", ".flac", ".mp3"}

bpm, conf = detect_bpm("file_path")
print(f"BPM: {bpm}, Confidence: {conf}")

def scan_folder(path):
    rows = []

    for file in Path(path).rglob("*"):
        if file.suffix.lower() not in AUDIO_EXTS:
            continue

        try:
            info = sf.info(file)
        except Exception:
            continue

        rows.append({
            "filename": file.name,
            "path": str(file),
            "duration_sec": round(info.duration, 3),
            "samplerate": info.samplerate,
            "channels": info.channels,
            "format": info.format
        })

    return rows
