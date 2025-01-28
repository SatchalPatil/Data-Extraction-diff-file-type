import streamlit as st
from docx import Document
import fitz
from PIL import Image
from pytesseract import pytesseract, Output
import pandas as pd
from bs4 import BeautifulSoup
import requests
from transformers import BlipProcessor, BlipForConditionalGeneration
from pdf2image import convert_from_path
from io import BytesIO

# Detect file type based on extension
def detect_file_type(file_path):
    file_extension = file_path.name.split('.')[-1].lower()
    if file_extension == "pdf":
        return "pdf"
    elif file_extension == "docx":
        return "docx"
    elif file_extension in ["xls", "xlsx"]:
        return "excel"
    elif file_extension in ["jpg", "jpeg", "png"]:
        return "image"
    else:
        return None

# Extract text from PDF (check for searchable text, fallback to OCR if necessary)
def extract_text_from_pdf(pdf_file):
    try:
        doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        # If no searchable text found, use OCR
        if not text.strip():
            st.warning("Searchable text not found in PDF. Using OCR to extract text.")
            pdf_file.seek(0)  # Reset file pointer for OCR
            text = extract_text_with_ocr(pdf_file)
        return text
    except Exception as e:
        return f"Error extracting text from PDF: {e}"

# OCR extraction for scanned PDFs
def extract_text_with_ocr(pdf_file):
    try:
        images = convert_from_path(pdf_file, dpi=300, fmt="jpeg")
        text = ""
        for image in images:
            text += pytesseract.image_to_string(image, lang="eng", output_type=Output.STRING)
        return text
    except Exception as e:
        return f"Error performing OCR on PDF: {e}"

# Extract text from DOCX
def extract_text_from_docx(docx_file):
    doc = Document(docx_file)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text.strip()

# Extract data from Excel
def extract_data_from_excel(excel_file):
    df = pd.read_excel(excel_file)
    return df.to_string(index=False)

# Extract text from image using BLIP
def extract_text_from_image(image_file):
    try:
        processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
        image = Image.open(image_file).convert("RGB")
        inputs = processor(image, return_tensors="pt")
        out = model.generate(**inputs)
        caption = processor.decode(out[0], skip_special_tokens=True)
        return caption
    except Exception as e:
        return f"Error processing image: {e}"

# Extract text from URL
def extract_news_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string.strip() if soup.title else "No Title Found"
        paragraphs = soup.find_all('p')
        content = "\n\n".join(para.get_text(strip=True) for para in paragraphs)
        return f"Title: {title}\n\nContent:\n\n{content}"
    except Exception as e:
        return f"Error extracting data from URL: {e}"

# Streamlit App
def main():
    st.title("Text Extraction App")
    st.write("Upload a file or enter a URL to extract text. You can also download the extracted text.")

    # Sidebar options
    input_type = st.sidebar.radio("Choose Input Type:", ("File", "URL"))

    extracted_text = ""

    if input_type == "File":
        uploaded_file = st.file_uploader("Upload a file:", type=["pdf", "docx", "xls", "xlsx", "jpg", "jpeg", "png"])
        if uploaded_file is not None:
            file_type = detect_file_type(uploaded_file)
            if file_type == "pdf":
                extracted_text = extract_text_from_pdf(uploaded_file)
            elif file_type == "docx":
                extracted_text = extract_text_from_docx(uploaded_file)
            elif file_type == "excel":
                extracted_text = extract_data_from_excel(uploaded_file)
            elif file_type == "image":
                extracted_text = extract_text_from_image(uploaded_file)
            else:
                extracted_text = "Unsupported file type."
            st.text_area("Extracted Text:", extracted_text, height=300)

    elif input_type == "URL":
        url = st.text_input("Enter the URL:")
        if url:
            extracted_text = extract_news_data(url)
            st.text_area("Extracted Text:", extracted_text, height=300)

    # Download functionality
    if extracted_text:
        st.markdown("---")
        st.subheader("Download Extracted Text")
        # Create a downloadable text file
        text_file = BytesIO()
        text_file.write(extracted_text.encode("utf-8"))
        text_file.seek(0)

        st.download_button(
            label="Download as .txt",
            data=text_file,
            file_name="extracted_text.txt",
            mime="text/plain"
        )

if __name__ == "__main__":
    main()
