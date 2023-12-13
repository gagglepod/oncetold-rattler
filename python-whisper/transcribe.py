import whisper
import os

# Set input and output file paths
input_file = "https://storage.googleapis.com/storage.oncetold.net/80000013/20800034/wy00-war-yankee-trailer-v2-2020.mp3"
# input_file = "../wy-trailer.mp3"
output_file = "wy-trailer-2023.srt"

# Load audio file using Whisper's Audio class
audio = whisper.audio.from_file(input_file)

# Transcribe audio using the 'tiny' model
transcriber = whisper.Transcriber(model="tiny")
transcript = transcriber.transcribe(audio)

# Format transcript as SRT
srt = ""
for i, line in enumerate(transcript.lines):
    start_time = line.start_time.strftime("%H:%M:%S,%f")[:-3]
    end_time = line.end_time.strftime("%H:%M:%S,%f")[:-3]
    text = line.text.replace("\n", "\\n")
    srt += f"{i+1}\n{start_time} --> {end_time}\n{text}\n\n"

# Save SRT file
with open(output_file, "w") as f:
    f.write(srt)

print(f"Transcript saved as {os.path.abspath(output_file)}")
