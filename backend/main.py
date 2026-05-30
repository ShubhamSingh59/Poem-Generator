from io import BytesIO

from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
from process.vision import VisionProcessor
from process.story import StoryGenerator
from process.audio import AudioTranscriber
from fastapi.responses import StreamingResponse

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

caption_generator = VisionProcessor()
story_generator = StoryGenerator()
audio_transcriber = AudioTranscriber()

@app.post("/api/generate-story")
async def generateStory(imgFile: UploadFile = File(...)):
    image_bytes = await imgFile.read()
    image = Image.open(BytesIO(image_bytes)).convert("RGB")
    
    caption = caption_generator.generate_caption(image)
    story = story_generator.generate_story(caption)
    audio = audio_transcriber.audio_generator(story)
    
    audio_buffer = BytesIO(audio)
    audio_buffer.seek(0)
    return StreamingResponse(audio_buffer, media_type="audio/wav")
    