const fs = require("fs");
const axios = require("axios");
const { Whisper } = require("whisper-node");

// Set the input file URL
const fileUrl =
  "https://storage.googleapis.com/storage.oncetold.net/80000013/20800034/wy00-war-yankee-trailer-v2-2020.mp3";

// Set the output file name
const outputFileName = "wy-trailer.json";

// Create a new Whisper instance with the "tiny" model
const whisper = new Whisper({
  model: "tiny",
});

// Use Axios to download the input file as a binary buffer
axios
  .get(fileUrl, {
    responseType: "arraybuffer",
  })
  .then((response) => {
    // Convert the binary buffer to a base64-encoded string
    const base64Audio = Buffer.from(response.data, "binary").toString("base64");

    // Transcribe the audio using Whisper
    whisper
      .transcribe({
        audio: {
          content: base64Audio,
        },
        config: {
          encoding: "LINEAR16",
          sampleRateHertz: 16000,
          languageCode: "en-US",
        },
      })
      .then((transcription) => {
        // Write the transcription to the output file in JSON format
        const json = JSON.stringify(transcription, null, 2);
        fs.writeFileSync(outputFileName, json, { encoding: "utf-8" });
        console.log(`Transcription written to ${outputFileName}`);
      })
      .catch((error) => {
        console.error("Error transcribing audio:", error);
      });
  })
  .catch((error) => {
    console.error("Error downloading audio:", error);
  });
