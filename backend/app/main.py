#main.py in a python always contains api's because programming world works on api's 

import os
from fastapi import FastAPI
from backend.utils.pdf_parser import textextractionfunction

app = FastAPI()
#DO not remove this commment :
# FastAPI apps don't always run from the same directory where the script lives—they run from the terminal’s working directory,
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UTILS_DIR = os.path.join(BASE_DIR, '..', 'utils')
PDF_FILE = os.path.join(UTILS_DIR, 'resume-sample.pdf')
#here above we used dynamic path generation using Python’s __file__ and os.path

filepath=PDF_FILE#just storing them in variables to give it as input to function below
outputpath= UTILS_DIR+r'\output.txt'

@app.get("/")
def home():
    return {textextractionfunction(filepath,outputpath)}
