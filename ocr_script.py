import pytesseract
import cv2
import os

# Set Tesseract path (keep this since it works for you)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Folders
image_folder = 'images'
output_folder = 'output_texts'

# Create output folder if not exists
os.makedirs(output_folder, exist_ok=True)

# Preprocessing function using OpenCV
def preprocess_image(img_path):
    img = cv2.imread(img_path)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur
    blur = cv2.GaussianBlur(gray, (3, 3), 0)

    # Apply thresholding (binarization)
    _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return thresh

# Process each image
for filename in os.listdir(image_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        img_path = os.path.join(image_folder, filename)
        print(f"🔍 Processing: {filename}")

        # Preprocess image
        processed_img = preprocess_image(img_path)

        # OCR on preprocessed image
        extracted_text = pytesseract.image_to_string(processed_img)

        # Save extracted text
        output_path = os.path.join(output_folder, f"{filename}.txt")
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(extracted_text)

        print(f"✅ Saved: {output_path}\n")
