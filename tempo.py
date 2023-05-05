import subprocess

input_file = "segment_0.mp3"
temp = "temp.mp3"
output_file = "segment_0_0.7.mp3"

tempo = "0.7"

command = ["ffmpeg", "-i", input_file, "-filter:a", f"atempo={tempo}", temp]

subprocess.run(command, check=True)

command = ["ffmpeg",  "-stream_loop", "-1", "-i", temp, "-c", "copy", "-t", "30", output_file]

subprocess.run(command, check=True)
