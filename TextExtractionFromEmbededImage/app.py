"""
app.py: Extracts text from embedded images in PDFs using Tesseract OCR.
"""
import sys
import ocrmypdf
import pytesseract
from PyPDF2 import PdfReader

# Optional: Set paths if you're using a virtual environment or Windows with custom install
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# -------------------------------
# Input/Output configuration
# -------------------------------
INPUT_PDF = "data/temp.pdf"         # 📝 Your input PDF with embedded Telugu + English text
OUTPUT_PDF = "data/output_ocr.pdf"   # 📝 OCR searchable PDF
TEMP_OUTPUT_TXT = "output_text.txt"  # Optional plain text output (post-processing)

# -------------------------------
# Run OCRmyPDF
# -------------------------------
try:
    ocrmypdf.ocr(
        INPUT_PDF,
        OUTPUT_PDF,
        language="tel+eng",   # Telugu + English
        force_ocr=True,       # Force OCR even if PDF has text
        deskew=True,          # Fix rotated/scanned pages
        optimize=1,           # Compression
        output_type="pdf",    # Can be 'pdf' or 'pdfa'
        progress_bar=True
    )

    print(f"✅ OCR completed. Output saved to: {OUTPUT_PDF}")

except ocrmypdf.exceptions.MissingDependencyError as e:
    print("❌ Missing dependency. Please ensure Tesseract and Ghostscript are installed.")
    sys.exit(1)
except ocrmypdf.exceptions.PriorOcrFoundError as e:
    print("⚠️ PDF already contains OCR. Skipping.")
    sys.exit(0)
except ocrmypdf.exceptions.EncryptedPdfError as e:
    print("🔐 Encrypted PDF. Cannot proceed.")
    sys.exit(1)
except Exception as e: # pylint: disable=broad-exception-caught
    print(f"❌ Error during OCR: {e}")
    sys.exit(1)


# -------------------------------
# Extract text from output PDF to text
# -------------------------------
try:

    reader = PdfReader(OUTPUT_PDF)
    with open(TEMP_OUTPUT_TXT, "w", encoding="utf-8") as f:
        for page in reader.pages:
            f.write(page.extract_text() or "")
            f.write("\n")

    print(f"✅ Extracted text written to {TEMP_OUTPUT_TXT}")
except Exception as e: # pylint: disable=broad-exception-caught
    print("⚠️ Skipping text extraction — PyPDF2 not installed. Run: pip install PyPDF2")
