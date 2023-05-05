import librosa
import soundfile
import os

song = r"./splits/symphony5original.mp3/segment_0.mp3"
y, sr = librosa.load(song)
pitch_var = [-10, -5, 0, 5, 10]
tempo_var = [0.7, 0.85, 1, ]

splits_folder_path = r"./splits"
for song_splits in os.listdir(splits_folder_path):
    # if os.path.isdir(os.path.join(splits_folder_path, song_splits)):
    for segment in song_splits:
        for i in range(len(pitch_var)):
            new_y = librosa.effects.pitch_shift(y, n_steps = pitch_var[i], sr = sr)
            soundfile.write(f"pitchShifted/song_{i}.mp3", new_y, sr)

        
        

for i in range(len(pitch_var)):
    new_y = librosa.effects.pitch_shift(y, n_steps = pitch_var[i], sr = sr)
    soundfile.write(f"pitchShifted/song_{i}.mp3", new_y, sr,)




