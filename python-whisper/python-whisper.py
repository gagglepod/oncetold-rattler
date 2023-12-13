import whisper

model = whisper.load_model("base")
# result = model.transcribe("../sample.mp3")

result = model.transcribe("https://storage.googleapis.com/storage.oncetold.net/80000013/20800034/wy00-war-yankee-trailer-v2-2020.mp3")
print(result["text"])