# import whisper

# transcribe audio file
# def transcribe():
#     model = whisper.load_model("tiny")

#     audio = whisper.load_audio("https://storage.googleapis.com/storage.oncetold.net/80000013/20800034/wy00-war-yankee-trailer-v2-2020.mp3")

#     result = model.transcribe(audio)
#     print(result["text"])

import whisper
import os

# Set input and output file paths
input_file = "https://storage.googleapis.com/storage.oncetold.net/80000013/20800034/wy00-war-yankee-trailer-v2-2020.mp3"
# input_file = "../podcasters-kit-12-hours-of-podcasting-live-interview.wav"
output_file = "podcast-design-webinar.srt"

# Load audio file using Whisper's Audio class
audio = whisper.load_audio(input_file)

# Transcribe audio using the 'tiny' model
transcriber = whisper.load_model("tiny")
transcript = transcriber.transcribe(audio)

# save the transcript in SRT format
srt = whisper.from_transcript(transcript)
with open("podcast-design-webinar.srt", "w") as f:
    f.write(srt)

print(f"Transcript saved as {os.path.abspath(output_file)}")
