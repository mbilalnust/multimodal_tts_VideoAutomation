# Multimodal TTS to Video Automation

## Overview

This project automates the creation of videos for platforms like YouTube and TikTok using text-to-speech (TTS) technology and the MoviePy library. The script reads text from a file, generates audio using TTS, and combines it with an image to create a video.

## Requirements

- Python 3.x
- `asyncio`
- `edge-tts`
- `moviepy`

You can install the required libraries using pip:

```bash
pip install edge-tts moviepy
```

## Usage

1. **Prepare your text**: Create a text file named `text.txt` in the project directory. This file should contain the text you want to convert to speech.

2. **Select a voice**: The script includes a list of available voices. You can modify the `VOICE` variable in the script to choose a different voice from the `VOICES` list.

3. **Set your image**: Replace the `IMAGE_FILE` variable with the path to your desired background image.

4. **Run the script**: Execute the script using Python:

   ```bash
   python test_2.py
   ```

5. **Output**: The script will generate an audio file named `output_audio.mp3` and a video file named `output_video.mp4` in the project directory.

## Code Explanation

- **Imports**: The script imports necessary libraries for asynchronous programming, TTS, and video creation.
  
- **Voice Selection**: A list of available voices is defined in the `VOICES` variable. You can choose any voice from this list.

- **Text Reading**: The script reads the content of `text.txt` and stores it in the `TEXT` variable.

- **Audio Generation**: The `amain` function uses the `edge_tts` library to convert the text to speech and save it as an audio file.

- **Video Creation**: The script uses MoviePy to create a video by combining the audio with an image. The commented-out section for adding text to the video can be uncommented if desired.

## Customization

Feel free to customize the script by changing the voice, text, image, and other parameters to suit your needs.