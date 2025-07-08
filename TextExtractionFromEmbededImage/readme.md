# Text Extraction From Embedded Image (#TextExtractionFromEmbeddedImage)

This project extracts text (including multilingual support like Telugu) from embedded images (JPG, PNG, PDF), detects language, and exports the result into a PDF using OCR.

---

## 🛠️ Setup Instructions

### 1. Install Dependencies

#### 🧠 Core Tools (manual installation required)

- **Tesseract OCR** (No installation required; portable binary is enough)  
  🔗 [Download for Windows](https://github.com/tesseract-ocr/tesseract)

- **Ghostscript** (Required for PDF processing)  
  🔗 [Download for Windows](https://ghostscript.com/releases/gsdnld.html)

- **Poppler** (Required by `pdf2image` for PDF to image conversion)  
  🔗 [Download Poppler for Windows](https://github.com/oschwartz10612/poppler-windows/releases)  
  ➤ Add the `bin/` folder to your system PATH  
  ➤ Or set `poppler_path = r"C:\path\to\poppler-xx\bin"` in your code

---

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Run the Application

```bash
python app.py
```

---

## ✅ Core Functional Requirements

| Package      | Purpose                                                       | Status       |
|--------------|---------------------------------------------------------------|--------------|
| `pdf2image`  | Converts PDF pages into images (JPG/PNG) for OCR              | ✅ Essential |
| `pytesseract`| Extracts text from images using Tesseract OCR                 | ✅ Essential |
| `pillow`     | Image processing backend (used by `pdf2image`, `pytesseract`) | ✅ Essential |
| `reportlab`  | Creates PDF files with custom text/formatting                 | ✅ Optional (if not using `ocrmypdf`) |
| `ocrmypdf`   | Adds searchable OCR layer to PDFs (preserves original layout) | ✅ Optional (alternative to `reportlab`) |
| `PyPDF2`     | Basic PDF manipulation (merge, split, etc.)                   | ✅ Optional |

---

## 🌐 Language Detection

| Package       | Purpose                            | Status         |
|---------------|------------------------------------|----------------|
| `langdetect`  | Detects language from extracted text | ✅ Recommended |

---

## 🔍 Code Quality & Security Tools

| Package   | Purpose                                               | Status         |
|-----------|-------------------------------------------------------|----------------|
| `pylint`  | Linting for code style, unused imports, etc.          | ✅ Recommended |
| `bandit`  | Security analysis of Python code                      | ✅ Recommended |

---


## 📁 File Structure (Optional Example)

```bash
TextExtractionFromEmbeddedImage/
├── app.py               # 🔹 Main OCR logic
├── requirements.txt     # 🔹 Python dependencies
├── README.md            # 🔹 This file
├── output/              # 🔹 Extracted PDF/text output
└── imagesdirectory/     # 🔹 Input images or PDFs
```

---

📌 _For best results, ensure your Tesseract supports the target language (`tel.traineddata` for Telugu, etc.)._


## 🚀 How to Execute
Follow these steps to check code quality, perform security validation, and run the application:

✅ Step 1: Style & Code Quality Check
pylint app.py

🔒 Step 2: Security Audit
bandit app.py

🧠 Step 3: Run the OCR Pipeline
python app.py
