import asyncio
import edge_tts
import os
import numpy as np
import soundfile as sf
import textwrap
import tempfile
from moviepy import AudioFileClip, ImageClip, TextClip, CompositeVideoClip
from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.video.io.VideoFileClip import VideoFileClip

VOICES = [
    'en-AU-NatashaNeural', 'ko-KR-SunHiNeural','en-AU-WilliamNeural',
    'en-CA-ClaraNeural', 'en-CA-LiamNeural',
    'en-GB-LibbyNeural', 'en-GB-MaisieN'
]
TEXT = ""
with open("text.txt", "r", encoding="utf-8") as file:
    TEXT = file.read()

VOICE = VOICES[1]
RATE = "+5%"
OUTPUT_AUDIO_FILE = "output_audio.mp3"
OUTPUT_VIDEO_FILE = "output_video.mp4"
SRT_FILE = "output_subtitles.srt"
IMAGE_FILE = "background_image.jpg"  # Replace with your image file

# Utility: Convert seconds to SRT format
def sec_to_srt_time(sec):
    ms = int((sec - int(sec)) * 1000)
    h = int(sec // 3600)
    m = int((sec % 3600) // 60)
    s = int(sec % 60)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"

# Step 1: Split text into lines (~80 characters)
lines = textwrap.wrap(TEXT, width=80, break_long_words=False)

# Step 2: Generate full audio + generate per-line durations for SRT
async def generate_audio_and_srt():
    srt_lines = []
    start_time = 0
    counter = 1

    for line in lines:
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp_audio:
            audio_path = tmp_audio.name

        tts = edge_tts.Communicate(line, VOICE, rate=RATE)
        await tts.save(audio_path)

        data, samplerate = sf.read(audio_path)
        duration = len(data) / samplerate
        end_time = start_time + duration

        srt_lines.append(
            f"{counter}\n{sec_to_srt_time(start_time)} --> {sec_to_srt_time(end_time)}\n{line}\n\n"
        )
        counter += 1
        start_time = end_time

        os.remove(audio_path)

    with open(SRT_FILE, "w", encoding="utf-8") as f:
        f.writelines(srt_lines)

    # Generate full audio
    communicate = edge_tts.Communicate(TEXT, VOICE, rate=RATE)
    await communicate.save(OUTPUT_AUDIO_FILE)

# Run async TTS and SRT generation
loop = asyncio.get_event_loop_policy().get_event_loop()
try:
    loop.run_until_complete(generate_audio_and_srt())
finally:
    loop.close()

# ----- DO NOT TOUCH MOVIEPY PART -----
audio_clip = AudioFileClip(OUTPUT_AUDIO_FILE)
image_clip = ImageClip(IMAGE_FILE).with_duration(audio_clip.duration)

video = CompositeVideoClip([image_clip]).with_audio(audio_clip)  
video.write_videofile(OUTPUT_VIDEO_FILE, fps=24)