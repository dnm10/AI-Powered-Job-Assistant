import pdfplumber
from pdf2image import convert_from_path
from PIL import Image
import pytesseract

#function to extract simple text from pdf
def extract_with_pdfplumber(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ''
    return text

#function to extract text if the pdf is flattned we need to apply ocr
def extract_with_ocr(file_path):
    images = convert_from_path(file_path)
    text = ""
    for img in images:
        text += pytesseract.image_to_string(img)
    return text

#final function to combine above two functions
def extract_text_from_any_pdf(file_path):
    text = extract_with_pdfplumber(file_path)
    if not text.strip():
        print("No text found with pdfplumber. Switching to OCR...")
        text = extract_with_ocr(file_path)
    return text





#Prefix the path with r to tell Python “treat backslashes literally”:

outpath= r'AI-Powered-Job-Assistant\backend\utils' #this is the location where output pdf will be stored

#this functions creates a file to store the extracted text
def save_text_to_file(text, output_path):
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"✅ Text successfully saved to {output_path}")
    except Exception as e:
        print(f"⚠️ Error saving file: {e}")

def textextractionfunction(file_path, output_path):
    text = extract_text_from_any_pdf(file_path)
    save_text_to_file(text, output_path)
    return text

#this is where we run the final function of this file 
if __name__ == "__main__":
    textextractionfunction(filepath, outputpath)