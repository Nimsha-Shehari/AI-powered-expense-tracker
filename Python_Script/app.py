from flask import Flask, request, jsonify
import pytesseract
from PIL import Image
import re
import requests
from io import BytesIO

app = Flask(__name__)
import pytesseract

# Specify the path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Adjust for your OS and installation path

# Function to extract raw text using Tesseract OCR
def extract_text_tesseract(image_path):
    try:
        print("Extracting text using Tesseract OCR...")
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image, lang="eng")
        return text
    except Exception as e:
        print(f"Error during text extraction: {e}")
        return None

# Function to parse items and prices using NLP
def parse_receipt_with_nlp(text):
    if not text:
        return [], None

    lines = text.splitlines()
    items = []
    total_price = None

    for line in lines:
        print(f"Processing line: {line}")

        # Match items with prices using regex
        match = re.match(r"^(.*?)(\d+\.\d{2})$", line)
        if match:
            item = match.group(1).strip()
            price = float(match.group(2))
            items.append({'name': item, 'price': price})

        # Match total (case insensitive)
        if 'total' in line.lower():
            total_match = re.search(r"\d+\.\d{2}", line)
            if total_match:
                total_price = float(total_match.group(0))

    return items, total_price

@app.route('/parse_receipt', methods=['POST'])
def parse_receipt():
    data = request.json
    image_url = data.get('image_url')

    if not image_url:
        return jsonify({'error': 'No image URL provided'}), 400

    try:
        # Download the image from the URL
        response = requests.get(image_url)
        image = BytesIO(response.content)

        # Step 1: Extract text using Tesseract
        text = extract_text_tesseract(image)
        if not text:
            return jsonify({'error': 'Failed to extract text from the image'}), 500

        # Step 2: Parse the items and total price
        items, total_price = parse_receipt_with_nlp(text)

        # Return the parsed data as JSON
        return jsonify({
            'items': items,
            'total_price': total_price
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
