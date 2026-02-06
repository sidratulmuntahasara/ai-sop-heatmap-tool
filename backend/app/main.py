from fastapi import FastAPI, UploadFile, File
from app.services.chunker import chunk_text
from app.services.ai_signals import analyze_chunks
from app.services.heatmap import generate_heatmap_data
from fastapi.middleware.cors import CORSMiddleware
from app.services.file_parser import extract_text_from_file

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze-sop")
async def analyze_sop(file: UploadFile = File(...)):
    file_bytes = await file.read()
    try:
        text = extract_text_from_file(file_bytes, file.filename)
    except ValueError as ve:
        return {"error": str(ve)}
    chunks = chunk_text(text)
    analysis = analyze_chunks(chunks)
    heatmap = generate_heatmap_data(chunks, analysis)

    return {
        "heatmap": heatmap,
        "stats": analysis["summary"]
    }
