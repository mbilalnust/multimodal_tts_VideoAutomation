import asyncio
import edge_tts
from moviepy import AudioFileClip, ImageClip, TextClip, CompositeVideoClip


VOICES = [
    'en-AU-NatashaNeural', 'ko-KR-SunHiNeural','en-AU-WilliamNeural',
    'en-CA-ClaraNeural', 'en-CA-LiamNeural',
    'en-GB-LibbyNeural', 'en-GB-MaisieN'
]
TEXT = ""
with open("text.txt", "r") as file:
    TEXT = file.read()

VOICE = VOICES[1]
OUTPUT_AUDIO_FILE = "output_audio.mp3"
OUTPUT_VIDEO_FILE = "output_video.mp4"
IMAGE_FILE = "background_image.jpg"  # Replace with your image file

async def amain() -> None:
    communicate = edge_tts.Communicate(TEXT, VOICE, rate='+5%')
    await communicate.save(OUTPUT_AUDIO_FILE)

loop = asyncio.get_event_loop_policy().get_event_loop()
try:
    loop.run_until_complete(amain())
finally:
    loop.close()

# Create video with audio and transcript
audio_clip = AudioFileClip(OUTPUT_AUDIO_FILE)
image_clip = ImageClip(IMAGE_FILE).with_duration(audio_clip.duration)

# Create a text clip for the transcript
# txt_clip = TextClip(
#     text=TEXT,
#     font_size=24,
#     color='white',
#     bg_color='black',
#     size=image_clip.size,
#     font="Arial"  # Specify a font available on your system
# ).with_position('bottom').with_duration(audio_clip.duration)

# Combine image, audio, and text
video = CompositeVideoClip([image_clip]).with_audio(audio_clip)  # Removed txt_clip
video.write_videofile(OUTPUT_VIDEO_FILE, fps=24)
