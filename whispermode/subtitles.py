import whisper
from whisper.utils import get_writer

url = 'https://storage.googleapis.com/storage.oncetold.net/80000013/20800034/wy00-war-yankee-trailer-v2-2020.mp3'

# audio = whisper.load_audio(url)

# filename = "wy-trailer.mp3"
filename = url.rsplit('/', 1)[-1]

input_directory = "."
input_file = f"{input_directory}/{filename}"
# input_file = f"/{filename}"

model = whisper.load_model("tiny") # or whatever model you prefer
print("Whisper model loaded.")
result = model.transcribe(audio=url, verbose = True, language = "en")

# result = model.transcribe(input_file)
output_directory = "."

# Save as a TXT file
txt_writer = get_writer("txt", output_directory)
txt_writer(result, input_file)

# Save as an SRT file
srt_writer = get_writer("srt", output_directory)
srt_writer(result, input_file)

# Save as an VTT file
# vtt_writer = get_writer("vtt", output_directory)
# vtt_writer(result, input_file)

# Save as a TSV file
# tsv_writer = get_writer("tsv", output_directory)
# tsv_writer(result, input_file)

# Save as a JSON file
json_writer = get_writer("json", output_directory)
json_writer(result, input_file)

# audio source
# path = whisper.load_audio("wy-trailer.mp3")
# # url = 'https://storage.googleapis.com/storage.oncetold.net/80000013/20800034/wy00-war-yankee-trailer-v2-2020.mp3'

# def transcribe_audio(path):        
#     model = whisper.load_model('tiny')  # Change this to your desired model
#     print("Whisper model loaded.")
#     transcribe = model.transcribe(audio=path, verbose = True, language = "en")
#     segments = transcribe['segments']

#     for segment in segments:
#         startTime = str(0)+str(timedelta(seconds=int(segment['start'])))+',000'
#         endTime = str(0)+str(timedelta(seconds=int(segment['end'])))+',000'
#         text = segment['text']
#         segmentId = segment['id']+1
#         segment = f"{segmentId}\n{startTime} --> {endTime}\n{text[1:] if text[0] is ' ' else text}\n\n"

#         srtFilename = os.path.join(r"C:\Transcribe_project", "your_srt_file_name.srt")
#         with open(srtFilename, 'a', encoding='utf-8') as srtFile:
#             srtFile.write(segment)

#     return srtFilename

# # output the final result to a file named "wy-trailer.srt"
# subs.save('wy-trailer.srt')
