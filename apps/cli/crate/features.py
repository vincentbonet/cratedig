def detect_bpm(file_path): 
    import librosa #Package for audio analysis

    try: 
        y, sr = librosa.load(file_path, mono=True)
    except Exception: 
        return None, 0.0 # Unable to load file
    
    duration_sec = len(y) / sr 
    if duration_sec < 1.0: 
        return None, 0.0 #Base case, too short to analyze