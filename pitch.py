import librosa
import soundfile

song = r"./splits/symphony5original.mp3/segment_0.mp3"
y, sr = librosa.load(song)
pitch_var = [-10, -5, 0, 5, 10]

for i in range(len(pitch_var)):
    new_y = librosa.effects.pitch_shift(y, n_steps = pitch_var[i], sr = sr)
    soundfile.write(f"pitchShifted/song_{i}.mp3", new_y, sr,)
