# 🧾 OCR Text Extractor 

An Optical Character Recognition (OCR) project to extract text from **receipt images** and convert it into structured data.  
This helps in automating expense tracking, invoice digitization, and financial record-keeping.

---

## 📌 Project Overview
- Collected **receipt images** from Kaggle dataset.  
- Preprocessed images using techniques like **grayscale conversion**, **thresholding**, and **noise removal**.  
- Applied **OCR** (Optical Character Recognition) to extract text fields (item names, prices, totals, etc.).  
- Post-processed extracted text for cleaning and formatting.  
- Exported results into structured **CSV/JSON** for analysis.

---

## 🛠️ Tech Stack
- **Python**
- **OpenCV** (image preprocessing)
- **Tesseract OCR (pytesseract)** (text extraction)
- **NumPy, Pandas** (data handling)
- **Matplotlib** (visualization)

---
### 📊 Results

- Extracted item details and prices from scanned receipts.
- Converted raw OCR text into structured tabular data.
- Achieved better accuracy by applying image preprocessing before OCR.
