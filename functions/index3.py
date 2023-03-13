import wave
from vosk import Model, KaldiRecognizer, SetLogLevel
import json
# open audio file
wf = wave.open("opto_sessions_ep_69_excerpt.wav", "rb")

# Initialize model
# You can find several models at https://alphacephei.com/vosk/models
# I decided to go with the largest vosk-model-en-us-0.22
model = Model("/Users/konstantin/Downloads/vosk-model-en-us-0.22/")
rec = KaldiRecognizer(model, wf.getframerate())

# To store our results
transcription = []

while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        # Convert json output to dict
        result_dict = json.loads(rec.Result())
        # Extract text values and append them to transcription list
        transcription.append(result_dict.get("text", ""))

# Get final bits of audio and flush the pipeline
final_result = json.loads(rec.FinalResult())
transcription.append(final_result.get("text", ""))

# merge or join all list elements to one big string
transcription_text = ' '.join(transcription)
print(transcription_text)