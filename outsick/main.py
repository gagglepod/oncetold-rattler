import os

# record audio
import sounddevice as sd
from scipy.io.wavfile import write

# transcribe
import whisper
import torch
import numpy as np

# GPT-3
import openai   
from dotenv import load_dotenv
load_dotenv()

# copy to clipboard
import pyperclip

# record audio
def record(duration):
    fs = 44100 # sample rate
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    print("Recording Audio - Speak Now!")
    sd.wait() # Wait until recording is finished
    print("Audio recording complete")
    write('output.mp3', fs, myrecording)

# transcribe audio file
def transcribe():
    torch.cuda.is_available()
    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

    model = whisper.load_model("tiny", device=DEVICE)
    print(
        f"Model is {'multilingual' if model.is_multilingual else 'English only'}"
        f"and has {sum(np.prod(p.shape) for p in model.parameters()):,} parameters."
    )

    audio = whisper.load_audio("output.mp3")
    audio = whisper.pad_or_trim(audio)
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    __ , probs = model.detect_language(mel)
    print(f"Detected languages: {max(probs, key=probs.get)}")

    options = whisper.DecodingOptions(language="en", without_timestamps=True, fp16 = False)
    result = whisper.decode(model, mel, options)
    print(result.text)

    result = model.transcribe('output.mp3')
    print(result["text"])


# generate email with gpt3
def generate_email(text):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.Completion.create(
        model = "text-davinci-002",
        prompt="Crate a kind and formal email for this reason: {text}",
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response["choices"][0]["text"]

def main():
    record(8)
    text = transcribe() # with whisper
    email = generate_email(text)
    print(email)
    pyperclip.copy(email)

if __name__ == "__main__":
    main()
