const { spawn } = require("child_process");
const ffmpeg = require("ffmpeg-static");
const whisper = require("whisper-api");
const { Storage } = require("@google-cloud/storage");

const storage = new Storage();

async function transcribeAudio(file) {
  // Load audio file and convert to WAV format using ffmpeg
  const tempWavFile = `/tmp/${file.name.split(".")[0]}.wav`;
  const ffmpegProcess = spawn(ffmpeg, [
    "-i",
    `/tmp/${file.name}`,
    "-vn",
    "-ar",
    "44100",
    "-ac",
    "2",
    "-b:a",
    "192k",
    tempWavFile,
  ]);
  await new Promise((resolve, reject) => {
    ffmpegProcess.on("exit", (code) => {
      if (code === 0) {
        resolve();
      } else {
        reject(new Error(`ffmpeg exited with code ${code}`));
      }
    });
  });

  // Use PyTorch and Whisper to transcribe audio
  const transcriptions = await whisper.transcribe(tempWavFile);

  // Save transcripts to files and upload to bucket
  const bucketName = "storage.oncetold.net";
  const fileExt = file.name.split(".").pop();
  const fileNameWithoutExt = file.name.slice(0, -fileExt.length - 1);
  for (const [ext, transcript] of Object.entries(transcriptions)) {
    const transcriptFile = `${fileNameWithoutExt}.${ext}`;
    await storage.bucket(bucketName).file(transcriptFile).save(transcript);
  }

  // Return transcripts in JSON format
  return { transcripts: transcriptions };
}

exports.handleMP3Upload = async (event, context) => {
  const file = event;
  if (!file.name.endsWith(".mp3")) {
    return;
  }

  // Download the file from the bucket to local storage
  const tempFile = `/tmp/${file.name}`;
  await storage
    .bucket(file.bucket)
    .file(file.name)
    .download({ destination: tempFile });

  // Transcribe the audio file and save transcripts to bucket
  const transcripts = await transcribeAudio(file);
  await storage.bucket(file.bucket).upload(tempFile, {
    destination: file.name,
  });
  for (const ext of [".json", ".srt", ".tsv", ".txt", ".vtt"]) {
    const transcriptFile = `${file.name
      .split(".")
      .slice(0, -1)
      .join("")}${ext}`;
    await storage
      .bucket(bucketName)
      .file(transcriptFile)
      .upload({
        destination: transcriptFile,
        resumable: false,
        metadata: {
          contentType: "text/plain",
        },
      });
  }
};
