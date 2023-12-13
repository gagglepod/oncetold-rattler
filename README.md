# Oncetold Rattler

OpenAI Whisper is a versatile and powerful tool for transcriptions and translations. In this tutorial, we have learned how to install Whisper on Windows, Mac, and Ubuntu. Also, we have analyzed the performances of the available models. Finally, we saw how to integrate Whisper with Python and Node.js. In a later tutorial, we’ll learn how to use Whisper’s more advanced features and how to add them to our programs.

---

## Because You Will Forget!

Note: Python 3.12 does not work with OpenAI Whisper or with PyTorch at the time of this update (December 2023). Make sure you are using Python 3.11.

1. In `Cmder` you need to start every Python command with `python`
2. Run `python -m pip install --upgrade pip` to update pip
3. Run `python -m pip install -U openai-whisper` to update whisper
4. You may need to run it from the GitHub repo [OpenAI-Whisper Project](https://pypi.org/project/openai-whisper/): `python -m pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git`
5. Finally, run `python -m whisper sample.mp3`

### Troubleshooting

1. Did you get `No module named 'torch' error`? Then try `python -m pip list` to see what is installed.
2. No `torch`? Install it `pip install torch`

### Resources:

- [openai/whisper Github Repo](https://github.com/openai/whisper)
- [How To Install And Deploy Whisper, The Best Open-Source Alternative To Google Speech-To-Text - October 26th, 2022](https://nlpcloud.com/how-to-install-and-deploy-whisper-the-best-open-source-alternative-to-google-speech-to-text.html)

---

If you want to read [How to train OpenAI GPT 3 model](https://techpro.ninja/how-to-train-openai-gpt-3/)

## openai-whisper-with-python-and-nodejs

OpenAI Whisper tutorial with Python and Node.js

A sample application based on OpenAI Whisper with Python and Node.js for my blog
[OpenAI Whisper tutorial with Python and Node.js](https://techpro.ninja/whisper-openai-tutorial-with-python-nodejs/). Installation details can be found on the blog

### Running the App

`whisper sample.mp3 --model tiny --device cpu --fp16 False`
`whisper story-hunting.mp3 --model tiny --device cpu --fp16 False`
`whisper wy-trailer.mp3 --model tiny --device cpu --fp16 False`
`whisper podcasters-kit.wav --model tiny --device cpu --fp16 False`

### Warnings

Using Whisper in Python 3.10 this warning may appear:

```shell
UserWarning: FP16 is not supported on CPU; using FP32 instead
```

This is a nuisance and should make fp32 the default on CPU without warning. However, to force FP32 and avoid this warning:

_Python_

`fp16=False`

_CLI_

`--fp16 False`

## Running the Whisper command line

Once the above step runs successfully, you are ready to extract the text from an audio file by running the following command:

`whisper sample.mp3`

```javascript
# Run the command
oncetold-rattler:~$ whisper sample.mp3
Detecting language using up to the first 30 seconds. Use `--language` to specify the language
Detected language: English
[00:00.000 --> 00:11.400]  It's May, 1864, and the Union has entered its fourth year of war against the Confederacy.
[00:11.400 --> 00:15.680]  President Abraham Lincoln has fired yet another general and is looking for an officer who
[00:15.680 --> 00:18.000]  will take the fight to the rebels.
[00:18.000 --> 00:23.200]  Enter Major General Ulysses S. Grant, the hero of Vicksburg, and the type of general Lincoln
[00:23.200 --> 00:28.240]  knows will change the direction of the war in favor of the United States of America.
[00:28.240 --> 00:33.520]  According to the rank of Lieutenant General, a rank only held in wartime by George Washington,
[00:33.520 --> 00:38.960]  Lincoln tasked Grant with the job of leading the Union troops against the Confederate Army.
[00:38.960 --> 00:43.280]  Grant wastes no time in forming a new aggressive strategy that will attack the Confederacy
[00:43.280 --> 00:48.680]  from five different directions and take him, the new commander of the Army of the Potomac,
[00:48.680 --> 00:54.160]  into the field to face General Lee and the Army of Northern Virginia.

# Output files
oncetold-rattler:$ ls
sample.mp3  sample.mp3.json  sample.mp3.srt  sample.mp3.tsv  sample.mp3.txt  sample.mp3.vtt
```

It takes some time to process the audio and generates five different formats, namely .json, .srt,.tsv, .txt, and .vtt.

## Customizing Whisper

If you write the following command on your terminal, you will see a lot of customization options for the input and output arguments. I will explain a few of the common arguments here so that it is easy for us to understand when we want to extract better results from Whisper.

`whisper --help`

- —model: This is how you select the model for your processing. Each of these models has been trained with a different number of parameters. In the next section, the parameters have been described in detail.

- –output_format: Select output format from the options: txt, vtt, srt, tsv, json, all. Default value is all

- –verbose: whether to print out the progress and debug messages (default: True)

- –task: Whether you want to transcriber translate (default: Transcribe). Transcribe does voice recognition whereas Translate changes from one language to another

- –language: Specify the language in the audio. If None is provided, language detection will be done.

- –temperature: Higher temperature values indicate how greedy the system has to become. By default, it is 0 and if the transcription is not good, we can gradually increase its value up to 1.

- –beam_size: number of beams in beam search, a heuristic search algorithm that explores a graph

- –best_of: number of candidates when sampling with non-zero temperature.

## OpenAI Whisper parameters

The performance of a model is determined by a variety of parameters. A model is regarded as good if it achieves high accuracy in production or test data and can generalize effectively to unknown data. The machine learning model parameters determine how the input data is transformed into the desired output. Whisper has 5 major models, each of which has been trained with a different number of parameters. Here is the list:

| Size   | Parameters | English-only model | Multilingual model | Required VRAM | Relative speed |
| ------ | ---------- | ------------------ | ------------------ | ------------- | -------------- |
| tiny   | 39 M       | tiny.en            | tiny               | ~1 GB         | ~32x           |
| base   | 74 M       | base.en            | base               | ~1 GB         | ~16x           |
| small  | 244 M      | small.en           | small              | ~2 GB         | ~6x            |
| medium | 769 M      | medium.en          | medium             | ~5 GB         | ~2x            |
| large  | 1550 M     | N/A                | large              | ~10 GB        | 1x             |

For Engish-only models, one can use models with .en extension which performs better. The difference in transcribing performance becomes less significant for the `small.en` and `medium.en` models. Here, the higher the number of parameters, the better the model’s performance. However, they consume more hardware resources, are slower, and incur more costs.

## OpenAI Whisper performance

The transcribing performance of Whisper is different for different languages. Below is the officially depicted performance graph on Zero-shot Word-Error-Rate (WER) published by OpenAI. Word Error Rate (WER) is a common metric for measuring the speech-to-text accuracy of automatic speech recognition (ASR) systems. Microsoft claims to have a word error rate of 5.1%. Google boasts a WER of 4.9%. For comparison, human transcriptionists average a word error rate of 4%. A 4% WER means, 96% of the transcript is correct.

As the metrics indicate above, WER in a lot of languages is very high, meaning they have a lot of transcription issues when used with Whisper. However, this can be improved by fine-tuning a model, which will be covered in another tutorial.

Whisper can be run both on CPU and GPU. However, with larger models, it is advisable to use GPU to boost your performance speed as it involves a lot of processing.

---

## Setting up Whisper with Python

If you want to learn how to set up Whisper with Node.js, you may skip this section and read on.

Integration of Whisper with Python is pretty straightforward. To transcribe a simple English speech into text, use the following code and save it as `transcribe.py`

```python
import whisper

model = whisper.load_model("base")
result = model.transcribe("sample.mp3")
print(result["text"])
```

In the program above, we load the base model for the sample.mp3 file we want to transcribe. Since there is no language option, it will automatically decode the language and print the text to the console. Now run the program as:

# Run the command

`oncetold-rattler:~$ python3 transcribe.py`

# Command Output

My thought I have nobody by a beauty and will as you poured. Mr. Rochester is sub in that so-don't find simplest, and devoted about, to what might in a-

That’s how you integrate the Whisper program with Python. We will learn advanced usage later in an upcoming tutorial.

---

## Setting up Whisper with Node.js

Integrating Node.js with Whisper is not a straightforward job, as there is no official SDK or API available. However, interacting with Whisper is not very difficult. The main idea behind the implementation lies in the fact that Node.js can interact with the Whisper command-line application.

The program depends on **child_process** which can be installed as

`npm install child_process`

Let’s create a program that interacts with the Whisper command line. Save the file as `nodewhisper.js`

```javascript
const { spawn } = require("child_process");

const outdata = spawn("whisper", ["sample.mp3"]);

outdata.stdout.on("data", (data) => {
  console.log(`stdout: ${data}`);
});

outdata.stderr.on("data", (data) => {
  console.log(`stderr: ${data}`);
});

outdata.on("error", (error) => {
  console.log(`error: ${error.message}`);
});

outdata.on("close", (code) => {
  console.log(`child process exited with code ${code}`);
});
```

In line 1 of the code above, the child_process module creates new child processes of our main Node.js process. We can execute shell commands with these child processes.

_In Line 2, we are calling the Whisper shell command using spawn() which streams all the shell output._

Run the command using:

# Run the command

`oncetold-rattler:~$ node nodewhisper.js`

## Command Output

My thought I have nobody by a beauty and will as you poured. Mr. Rochester is sub in that so-don't find simplest, and devoted about, to what might in a-

---

## Language Detection

For language identification, you first need to load the audio using the load_audio() method from the whisper module. Next, you pad or trim the audio using the pad_or_trim() method, which pads or trims your audio file to the specified duration. The default size is 30 seconds.

```javascript
audio = whisper.load_audio("wy-trailer.mp3");
audio = whisper.pad_or_trim(audio);
```

Whisper models are statistical algorithms that work with numbers. You must convert audio data to numbers before Whisper models can process it. You can use the Log Mel Spectrogram technique for the numerical feature representation of audio signals.

The following code creates a feature representation of your audio file using the _log_mel_spectrogram()_ method and then moves the feature map to the same device as the model.

You can then use the _detect_language()_ method of the model object and pass the feature map to it. In the output, you will see the detection probability for various languages.

```javascript
mel = whisper.log_mel_spectrogram(audio).to(model.device);

_, (probs = model.detect_language(mel));
probs;
```

You can see that the English language (en) has the highest probability of 99.7%, followed by Chinese (zh) and German (de).

Note: The language codes follow ISO-639-1 standard language codes.

You can get the language with the highest probability using the following script.

```javascript
print(f"Detected language: {max(probs, key=probs.get)}")
```

---

## Transcribing Earnings Calls with OpenAI Whisper

Earnings calls are like an “inside look” into how publicly traded companies are doing financially. These calls can significantly impact the company’s stock price, making them critical for investors and stakeholders.

With Whisper, you can quickly transcribe these calls, so you don’t miss a beat! Plus, you can quickly summarize the call’s content, identify critical information, and even track the company’s financial performance over time. In this section, you’ll see how to use Whisper to transcribe Microsoft’s Q4 earnings call in 2022 – it’s easier than you think!

[For More Info](https://analyzingalpha.com/openai-whisper-python-tutorial)

---

## Trim Earnings Calls with FFMPEG

If you open the YouTube video, you will see that the presentation starts at 32:04 seconds and ends at 1:13:59 seconds. The video contains random music followed by a short introduction before 32:04 seconds. The presentation ends at 1:13:59, followed by a question/answer session.

I will only transcribe the presentation. You can transcribe the Q&A session as well if you want.

For trimming the earnings call, I will use FFMPEG, a free, open-source command-line tool for cutting audio, video, and multimedia files. It is a cross-platform software that can be used on different operating systems like Windows, macOS, and Linux.

The FFMPEG official website explains the installation process for FFMPEG binaries.

[For More Info](https://analyzingalpha.com/openai-whisper-python-tutorial)

## Using Oncetold-Rattler Whisper Tools:

1. Change the input file and use node-whisper:
   `npm run dev`

2. Run `whisper` direct from the command line:
   `whisper wy-trailer.mp3 --model tiny --device cpu --fp16 False`
