import librosa
import soundfile
import os
import subprocess


pitch_var = [-10, -5, 0, 5, 10]
tempo_var = [0.7, 0.85, 1, 1.15, 1.3]

splits_folder_path = r"./splits"
song_number = 0

for song_splits in os.listdir(splits_folder_path):

    segment_number = 0
    for segment in os.listdir(os.path.join(splits_folder_path, song_splits)):

        song = os.path.join(splits_folder_path, song_splits, segment)
        y, sr = librosa.load(song)
        variation = 0
        for pitch in pitch_var:

            new_y = librosa.effects.pitch_shift(y, n_steps = pitch, sr = sr)
            soundfile.write(f"generated/song.mp3", new_y, sr)
            input_file = "generated/song.mp3"
            temp = "generated/temp.mp3"
            path = os.path.join("generated", f"song_{song_number}", f"segment_{segment_number}")
            os.makedirs(path, exist_ok = True)

            for tempo in tempo_var:

                output_file = f"generated/song_{song_number}/segment_{segment_number}/sample_{variation}.mp3"
                subprocess.run(["rm", "./generated/temp.mp3"])
                command = ["ffmpeg", "-i", input_file, "-filter:a", f"atempo={tempo}", temp]
                subprocess.run(command, check = True)
                command = ["ffmpeg",  "-stream_loop", "-1", "-i", temp, "-c", "copy", "-t", "30", output_file]
                subprocess.run(command, check = True)
                variation += 1

            subprocess.run(["rm", "./generated/song.mp3"], check = True)
            # subprocess.run(["rm", "./generated/temp.mp3"], check = True)

        segment_number += 1
    song_number += 1

subprocess.run(["rm", "./generated/temp.mp3"])
