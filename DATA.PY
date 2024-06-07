import fitz  # PyMuPDF
import csv

# Open the PDF file
pdf_document = "1-300.pdf"
document = fitz.open(pdf_document)

# Prepare a CSV file to write the data
csv_file = "extracted_data.csv"
csv_columns = ["Name of Issuer", "Sub Type", "Instrument Type", "Amount (Rs.Mn)", "Rating", "Industry Name", "Basic Industry"]

with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(csv_columns)

    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text = page.get_text("text")

        # Split the text into lines
        lines = text.split('\n')

        # Process lines to extract the required data
        for line in lines:
            # Sample processing (exact processing will depend on the PDF structure)
            if line.strip() and len(line.split()) > 6:
                data = line.split()
                writer.writerow(data[:7])

print("Data extraction to CSV completed.")
