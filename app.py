from flask import Flask, render_template, request
import pytesseract
import cv2
import os

# Required for Windows (if not in PATH)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload and output folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs('output_texts', exist_ok=True)

def preprocess_image(img_path):
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 0)
    _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return thresh

@app.route('/', methods=['GET', 'POST'])
def index():
    extracted_text = None
    if request.method == 'POST':
        image_file = request.files['image']
        if image_file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], image_file.filename)
            image_file.save(filepath)

            processed_img = preprocess_image(filepath)
            extracted_text = pytesseract.image_to_string(processed_img)

            # Save to .txt file (optional)
            output_path = os.path.join('output_texts', f"{image_file.filename}.txt")
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(extracted_text)

    return render_template('index.html', text=extracted_text)

if __name__ == '__main__':
    app.run(debug=True)
