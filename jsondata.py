import fitz 
import json

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    all_text = []
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text = page.get_text()
        all_text.append(text)
    return all_text

# Function to convert text content to JSON
def text_to_json(text_list):
    json_data = {
        "pages": []
    }
    for i, text in enumerate(text_list, start=1):
        page_data = {
            "page_number": i,
            "content": text.strip()
        }
        json_data["pages"].append(page_data)
    return json_data

# Extract text from the PDF
pdf_path = "pdffile.pdf"
extracted_text = extract_text_from_pdf(pdf_path)

# Convert text to JSON
json_data = text_to_json(extracted_text)

# Save JSON data to a file
json_filename = "pdffile.json"
with open(json_filename, "w") as json_file:
    json.dump(json_data, json_file, indent=4)

print("PDF content has been converted to JSON and saved to:", json_filename)

