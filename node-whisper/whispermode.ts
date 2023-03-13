const whisper = require("whisper-node");

const params = {
  filePath: "https://storage.googleapis.com/storage.oncetold.net/80000013/20800034/wy00-war-yankee-trailer-v2-2020.mp3", // required
  model:    "medium",             // default
  output:   "JSON",               // default
}

const transcript = await whisper(params);
