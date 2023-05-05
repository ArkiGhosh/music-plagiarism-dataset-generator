from pydub import AudioSegment
import numpy as np
import os

folder_path = r"./inputs"
for filename in os.listdir(folder_path):
    if os.path.isfile(os.path.join(folder_path, filename)):
        song = AudioSegment.from_file(os.path.join(folder_path, filename), format="mp3")

song_data = np.array(song.get_array_of_samples())
segment_length = 60 * song.frame_rate  # 30 seconds

segments = []
start = 0
while start + segment_length < len(song_data):
    end = start + segment_length
    segment = song_data[start:end]
    segments.append(segment)
    start += segment_length

for i, segment in enumerate(segments):
    segment = AudioSegment(
        segment.tobytes(),
        frame_rate=song.frame_rate,
        sample_width=song.sample_width,
        channels=song.channels,
    )
    os.makedirs(f"splits/{filename}", exist_ok=True)
    segment.export(f"splits/{filename}/segment_{i}.mp3", format="mp3")
    if (i == 2):
        break




