import io
import re
import pdfplumber
import docx
from PIL import Image
import pytesseract


# --------------------------------------
# CLEAN TEXT
# --------------------------------------

def clean_text(text):

    if not text:
        return ""

    text = text.lower()

    text = re.sub(r"[^\w\s\+\#\.\-]", " ", text)

    text = re.sub(r"\s+", " ", text)

    return text.strip()


# --------------------------------------
# PDF PARSER
# --------------------------------------

def parse_pdf(file_bytes):

    text = ""

    try:

        with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

    except Exception as e:
        print("PDF parsing error:", e)

    return text


# --------------------------------------
# DOCX PARSER
# --------------------------------------

def parse_docx(file_bytes):

    text = ""

    try:

        document = docx.Document(io.BytesIO(file_bytes))

        for para in document.paragraphs:
            text += para.text + "\n"

    except Exception as e:
        print("DOCX parsing error:", e)

    return text


# --------------------------------------
# IMAGE PARSER (OCR)
# --------------------------------------

def parse_image(file_bytes):

    text = ""

    try:

        image = Image.open(io.BytesIO(file_bytes))

        text = pytesseract.image_to_string(image)

    except Exception as e:
        print("Image OCR error:", e)

    return text


# --------------------------------------
# MAIN UNIVERSAL PARSER
# --------------------------------------

def parse_resume(uploaded_file):

    if uploaded_file is None:
        return ""

    filename = uploaded_file.name.lower()

    file_bytes = uploaded_file.read()

    raw_text = ""

    if filename.endswith(".pdf"):

        raw_text = parse_pdf(file_bytes)

    elif filename.endswith(".docx"):

        raw_text = parse_docx(file_bytes)

    elif filename.endswith((".jpg", ".jpeg", ".png")):

        raw_text = parse_image(file_bytes)

    else:

        print("Unsupported format")

    cleaned = clean_text(raw_text)

    return cleaned