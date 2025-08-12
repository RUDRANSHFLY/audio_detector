from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from coordinator import runAll

app = FastAPI()

class DetectRequest(BaseModel):
    audio_file_path : str

@app.get("/")
def read_root():
    return "Leo Eve"

@app.post('/detect/language')
def detect_language(req : DetectRequest):
    results = runAll(req.audio_file_path)
    return {
        "results" : results
    }