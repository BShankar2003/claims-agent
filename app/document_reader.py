import os
import pdfplumber

def read_document(file_path: str) -> str:
    if not os.path.exists(file_path):
        raise FileNotFoundError("Input file not found")

    if file_path.lower().endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    if file_path.lower().endswith(".pdf"):
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + "\n"
        return text

    raise ValueError("Unsupported file format. Use PDF or TXT.")
