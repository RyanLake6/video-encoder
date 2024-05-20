# Video-Formatter

[![License](https://img.shields.io/github/license/RyanLake6/your-repository)](https://github.com/RyanLake6/your-repository/blob/main/LICENSE)

This cli tool is meant to be an easy way for reformatting video encodings of a large group of videos. It utilizes [ffmpeg](https://ffmpeg.org/) to re-encode the videos.

I personally found running ffmpeg manually on a large set of files to be tedious especially with hardware constraints slowing down the encodings. Feel free to use this script for yourself.

**Ease of Life**: It will return all live ffmpeg updates as well as return how much data was saved and logs at the end

## Installation

Clone the repository or download the script.

```bash
git clone https://github.com/yourusername/video-reformatter.git
```

Navigate to the directory where the script is located.

```bash
cd video-reformatter
```

## Quick Use Guide (Windows)

_Assumes you have python and FFmpeg installed and added to system path_

Download the source code and enter the folder to run the following:

```bash
python .\reformat-videos.py -f "C:\Users\Ryan Lake\Documents\Tech Projects\clips"
```

### Command Line Arguments

- -f, --folder (required): The absolute path to the folder containing the video files.
- -d, --delete (optional): If supplied, deletes the original files after reformatting.
- -e, --encoding (optional): The encoding to use for the videos. Default is libx264 (H.264).
- -b, --bitrate (optional): Manually set the bitrate for encoding. If not provided, the original bitrate will be preserved.

TODO

- keep track of how much space is saved metric
- Store and return a full array of all things done for ease of viewing
