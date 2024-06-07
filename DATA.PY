import PyPDF2
import json

def pdf_to_json(pdf_path):
    # Open the PDF file
    with open(pdf_path, 'rb') as file:
        # Create a PDF reader object
        reader = PyPDF2.PdfReader(file)

        # Initialize an empty list to store extracted data
        data = []

        # Loop through each page in the PDF
        for page_num in range(len(reader.pages)):
            # Extract text from the page
            page = reader.pages[page_num]
            text = page.extract_text()

            # Process the extracted text (you may need to customize this part)
            # For example, split the text into lines and store in a dictionary
            page_data = {
                "page_number": page_num + 1,
                "text": text.strip()  # Remove leading/trailing whitespace
            }

            # Append page data to the list
            data.append(page_data)

    # Convert the extracted data to JSON
    json_data = json.dumps(data, indent=4)

    return json_data

# Provide the path to your PDF file
pdf_path = 'pdffile.pdf'

# Convert PDF to JSON
json_data = pdf_to_json(pdf_path)

# Save JSON data to a file
with open('outputdata.json', 'w') as json_file:
    json_file.write(json_data)

print("PDF data has been successfully converted to JSON.")
