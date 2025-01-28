# Streamlit Application for File and URL Data Extraction

## **Overview**
This Streamlit application provides a user-friendly interface to extract text data from various sources, including files (PDFs, images, Word documents, Excel spreadsheets) and URLs. The app also includes functionality to handle scanned PDFs using OCR and allows users to download the extracted text.

---

## **Features**
1. **File Input**
   - Supported file types:
     - PDFs (searchable and scanned)
     - Word documents (.docx)
     - Excel files (.xlsx, .csv)
     - Images (.jpg, .jpeg, .png)
   - Automatically detects the file type and applies the appropriate extraction method.

2. **URL Input**
   - Extracts text content from static HTML pages.
   - Limits horizontal text length for better readability using text wrapping.

3. **PDF Handling**
   - **Searchable PDFs**: Uses PyMuPDF (Fitz) for accurate text extraction.
   - **Scanned PDFs**: Applies PyTesseract OCR when no searchable text is found.

4. **Image Handling**
   - Converts images to RGB format using Pillow (PIL) and performs image captioning with the BLIP model.

5. **Excel Handling**
   - Extracts data from Excel and CSV files using Pandas.

6. **Word Document Handling**
   - Parses text from Word documents using the python-docx library.

7. **Text Download Functionality**
   - Users can download the extracted text as a `.txt` file.

---

## **Technologies Used**
- **Streamlit**: For building the user interface.
- **PyMuPDF (Fitz)**: For extracting text from searchable PDFs.
- **PyTesseract**: For OCR on scanned PDFs and image-based text extraction.
- **Pillow (PIL)**: For handling image preprocessing.
- **BLIP Model**: For image captioning.
- **Pandas**: For extracting data from Excel files.
- **python-docx**: For extracting text from Word documents.
- **BeautifulSoup & Requests**: For parsing HTML content from URLs.

---

## **Installation**
### Prerequisites:
- Python 3.8 or later installed on your machine.
- Virtual environment setup.

### Steps:
1. Clone the repository:
   ```bash
   git clone [<repository-link>](https://github.com/SatchalPatil/Data-Extraction-diff-file-type/tree/main)
   cd <repository-folder>
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run dataextraction.py
   ```

4. Open the provided local URL in your browser to access the app.

---

## **How to Use**
1. **Select Input Type**: Choose between uploading a file or entering a URL.
2. **Provide Input**:
   - For files, upload the desired document (PDF, Word, image, etc.).
   - For URLs, paste the link into the provided text box.
3. **Extract Text**: Click on the "Extract" button to process the input.
4. **Download Text**: Once extraction is complete, click the "Download" button to save the text file.

---

## **File Type Handling**
- **PDFs**:
  - Extracts text from searchable PDFs using PyMuPDF.
  - Applies OCR for scanned PDFs if searchable text is not found.
- **Images**:
  - Converts images to RGB format for compatibility with the BLIP model.
  - Generates image captions using the BLIP model.
- **Word Documents**:
  - Parses paragraphs and extracts text into a single string.
- **Excel Files**:
  - Reads Excel or CSV files and extracts tabular data.
- **URLs**:
  - Scrapes web page content using BeautifulSoup and Requests.

---

## **Future Enhancements**
1. Support for additional file types, such as plain text and Markdown.
2. Add multi-language OCR support for scanned PDFs.
3. Improve user experience with progress bars for large file uploads.
4. Include additional image processing capabilities, such as object detection.

---

## **License**
This project is open-source and licensed under the MIT License. Feel free to contribute and modify as needed.

---

For questions or issues, please contact satchalpatil04@gmail.com or open an issue in the GitHub repository.

