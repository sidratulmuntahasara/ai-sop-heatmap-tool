import pdfplumber
from docx import Document
from io import BytesIO

def extract_text_from_file(file_bytes, filename):
    """
    Detect file type and extract text accordingly
    Supports: .txt, .pdf, .docx
    """
    text = ""

    if filename.lower().endswith(".txt"):
        try:
            text = file_bytes.decode("utf-8")
        except UnicodeDecodeError:
            text = file_bytes.decode("cp1252", errors="replace")

    elif filename.lower().endswith(".pdf"):
        with pdfplumber.open(BytesIO(file_bytes)) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
            text = "\n\n".join(filter(None, pages))

    elif filename.lower().endswith(".docx"):
        doc = Document(BytesIO(file_bytes))
        paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
        text = "\n\n".join(paragraphs)

    else:
        raise ValueError("Unsupported file type. Use .txt, .pdf or .docx")

    return text
