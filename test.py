import asyncio
import edge_tts

VOICES = ['en-AU-NatashaNeural', 'en-AU-WilliamNeural', 'en-CA-ClaraNeural', 'en-CA-LiamNeural', 'en-GB-LibbyNeural', 'en-GB-MaisieN']
# TEXT = "Hello! Don't forget to like the video if you find it helpful, thank you"
# ... existing code ...
TEXT = ""
with open("text.txt", "r") as file:
    TEXT = file.read()
# ... existing code ...

VOICE = VOICES[1]
OUTPUT_FILE = "test_speed.mp3"

async def amain() -> None:
    communicate = edge_tts.Communicate(TEXT, VOICE)
    await communicate.save(OUTPUT_FILE)

loop = asyncio.get_event_loop_policy().get_event_loop()
try:
    loop.run_until_complete(amain())
finally:
    loop.close()
