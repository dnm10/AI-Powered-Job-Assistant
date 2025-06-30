import os
import sys
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse

# Ensure the utils and app directories are in sys.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UTILS_DIR = os.path.join(BASE_DIR, '..', 'utils')
APP_DIR = BASE_DIR
sys.path.append(os.path.abspath(UTILS_DIR))
sys.path.append(os.path.abspath(APP_DIR))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from backend.utils.pdf_parser import textextractionfunction
from tfidf_analyzer import analyze_resume_with_tfidf

app = FastAPI()

OUTPUT_DIR = os.path.join(UTILS_DIR, 'output')
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.post("/analyze-resume/")
async def analyze_resume(file: UploadFile = File(...)):
    try:
        file_path = os.path.join(OUTPUT_DIR, file.filename)
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)
        output_path = os.path.join(OUTPUT_DIR, f"{file.filename}.txt")
        resume_text = textextractionfunction(file_path, output_path)
        tfidf_result = analyze_resume_with_tfidf(resume_text)
        try:
            os.remove(file_path)
            os.remove(output_path)
        except Exception:
            pass
        return JSONResponse(content={
            "extracted_text": resume_text,
            "tfidf_analysis": tfidf_result
        })
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": f"Processing failed: {str(e)}"})

@app.get("/")
def home():
    return {"message": "Resume Analyzer API is running!"}