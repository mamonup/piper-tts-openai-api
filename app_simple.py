from fastapi import FastAPI
from fastapi.responses import Response
from pydantic import BaseModel, Field
import subprocess
import os
import uuid
import tempfile
from typing import Literal

app = FastAPI()

# Constants
PIPER_PATH = "piper.exe"
VOICE_MODEL_PATH = "piper_models/REPLACE_MODEL_HERE.onnx"
TEMP_DIR = tempfile.gettempdir()

class TTSRequest(BaseModel):
    model: str
    input: str
    voice: str = "alloy"
    response_format: Literal["mp3", "wav"] = "mp3"
    speed: float = 1.0

@app.post("/v1/audio/speech")
async def create_speech(request: TTSRequest):
    output_file = os.path.join(TEMP_DIR, f"{str(uuid.uuid4())}.{request.response_format}")
    
    # Prepare and execute Piper command
    command = [
        PIPER_PATH,
        "--model", VOICE_MODEL_PATH,
        "--output_file", output_file,
        "--length-scale", str(1.0/request.speed)
    ]

    subprocess.run(
        command,
        input=request.input,
        text=True,
        capture_output=True
    )

    # Read and return the audio file
    with open(output_file, 'rb') as f:
        content = f.read()
    
    # Clean up
    os.remove(output_file)

    return Response(
        content=content,
        media_type=f"audio/{request.response_format}",
        headers={
            'Content-Disposition': f'attachment; filename="speech.{request.response_format}"'
        }
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5002)