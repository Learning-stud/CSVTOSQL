# import re
# import mysql.connector
# from PyPDF2 import PdfReader
# from tabulate import tabulate

# # Step 1: Extract data from PDF
# import re
# import mysql.connector
# from PyPDF2 import PdfReader
# from tabulate import tabulate

# # Step 1: Extract data from PDF
# def extract_text_from_pdf(pdf_path):
#     pdf_reader = PdfReader(open(pdf_path, 'rb'))
#     text = ''
#     for page in pdf_reader.pages:
#         text += page.extract_text()
#     return text

# # Step 2: Process and format data
# def process_text(text):
#     # Print extracted text to analyze its structure
#     print("Extracted Text:")
#     print(text)

#     # Adjust this pattern based on the actual text structure
#     pattern = re.compile(
#         r"(\d+\s+[A-Za-z &.]+\s+[A-Za-z]+\s+[A-Za-z]+\s+[\d.]+\s+CARE\s+[A-Za-z0-9+();-]+\s+[A-Za-z &]+\s+[A-Za-z &]+)"
#     )
#     matches = pattern.findall(text)

#     # Debugging: Print matches to understand the data structure
#     print("Matches:")
#     print(matches)

#     data = []
#     for match in matches:
#         parts = match.split()
#         print("Parts:", parts)  # Debugging: Print parts to understand the split result

#         # Adjust these indices based on the actual structure
#         try:
#             care_index = parts.index('CARE')
#             name_of_issuer = " ".join(parts[1:care_index - 3])  # Adjust range based on actual structure
#             sub_type = parts[care_index - 3]
#             instrument_type = parts[care_index - 2]
#             amount = parts[care_index - 1].replace(',', '')  # Remove any commas from amount
#             rating = " ".join(parts[care_index:care_index + 2])  # Adjust range based on actual structure
#             industry_name = parts[care_index + 2]
#             basic_industry = parts[care_index + 3]
#             data.append((name_of_issuer, sub_type, instrument_type, amount, rating, industry_name, basic_industry))
#         except IndexError as e:
#             print(f"IndexError: Skipping invalid match: {match}. Error: {e}")
#         except ValueError as e:
#             print(f"ValueError: Skipping invalid match: {match}. Error: {e}")

#     # Debugging: Print final parsed data
#     print("Parsed Data:")
#     print(data)

#     return data

# # Step 3: Insert data into MySQL
# def insert_data_to_mysql(data):
#     db = mysql.connector.connect(
#         host="127.0.0.1",
#         user="root",
#         password="jaygajjar",
#         database="care_ratings"
#     )
#     cursor = db.cursor()

#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS ratings (
#             id INT AUTO_INCREMENT PRIMARY KEY,
#             name_of_issuer VARCHAR(255),
#             sub_type VARCHAR(255),
#             instrument_type VARCHAR(255),
#             amount DECIMAL(20, 2),
#             rating VARCHAR(50),
#             industry_name VARCHAR(255),
#             basic_industry VARCHAR(255)
#         )
#     ''')

#     sql = '''INSERT INTO ratings (name_of_issuer, sub_type, instrument_type, amount, rating, industry_name, basic_industry)
#              VALUES (%s, %s, %s, %s, %s, %s, %s)'''

#     cursor.executemany(sql, data)
#     db.commit()
#     cursor.close()
#     db.close()

# # Step 4: Fetch and display data from MySQL
# def fetch_and_display_data():
#     db = mysql.connector.connect(
#         host="127.0.0.1",
#         user="root",
#         password="jaygajjar",
#         database="care_ratings"
#     )
#     cursor = db.cursor()

#     cursor.execute('SELECT * FROM ratings')
#     rows = cursor.fetchall()

#     print("ID | Name of Issuer | Sub Type | Instrument Type | Amount | Rating | Industry Name | Basic Industry")
#     print("--------------------------------------------------------------------------------------------")
#     table = []
#     for row in rows:
#         table.append(row)

#     print(tabulate(table, headers=["ID", "Name of Issuer", "Sub Type", "Instrument Type", "Amount", "Rating", "Industry Name", "Basic Industry"], tablefmt="grid"))

#     cursor.close()
#     db.close()

# if __name__ == "__main__":
#     pdf_path = 'pdffile.pdf'  # Update this to the correct path if needed
#     text = extract_text_from_pdf(pdf_path)
#     data = process_text(text)
#     if data:  # Only insert data if it's non-empty
#         insert_data_to_mysql(data)
#         fetch_and_display_data()
#     else:
#         print("No data to insert.")


# # Step 2: Process and format data
# def process_text(text):
#     # Print extracted text to analyze its structure
#     print("Extracted Text:")
#     print(text)

#     # Adjust this pattern based on the actual text structure
#     pattern = re.compile(
#         r"(\d+\s+[A-Za-z &.]+\s+[A-Za-z]+\s+[A-Za-z]+\s+[\d.]+\s+CARE\s+[A-Za-z0-9+();-]+\s+[A-Za-z &]+\s+[A-Za-z &]+)"
#     )
#     matches = pattern.findall(text)

#     # Debugging: Print matches to understand the data structure
#     print("Matches:")
#     print(matches)

#     data = []
#     for match in matches:
#         parts = match.split()
#         print("Parts:", parts)  # Debugging: Print parts to understand the split result

#         # Adjust these indices based on the actual structure
#         try:
#             care_index = parts.index('CARE')
#             name_of_issuer = " ".join(parts[1:care_index - 3])  # Adjust range based on actual structure
#             sub_type = parts[care_index - 3]
#             instrument_type = parts[care_index - 2]
#             amount = parts[care_index - 1].replace(',', '')  # Remove any commas from amount
#             rating = " ".join(parts[care_index:care_index + 2])  # Adjust range based on actual structure
#             industry_name = parts[care_index + 2]
#             basic_industry = parts[care_index + 3]
#             data.append((name_of_issuer, sub_type, instrument_type, amount, rating, industry_name, basic_industry))
#         except IndexError as e:
#             print(f"IndexError: Skipping invalid match: {match}. Error: {e}")
#         except ValueError as e:
#             print(f"ValueError: Skipping invalid match: {match}. Error: {e}")

#     # Debugging: Print final parsed data
#     print("Parsed Data:")
#     print(data)

#     return data

# # Step 3: Insert data into MySQL
# def insert_data_to_mysql(data):
#     db = mysql.connector.connect(
#         host="127.0.0.1",
#         user="root",
#         password="jaygajjar",
#         database="care_ratings"
#     )
#     cursor = db.cursor()

#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS ratings (
#             id INT AUTO_INCREMENT PRIMARY KEY,
#             name_of_issuer VARCHAR(255),
#             sub_type VARCHAR(255),
#             instrument_type VARCHAR(255),
#             amount DECIMAL(20, 2),
#             rating VARCHAR(50),
#             industry_name VARCHAR(255),
#             basic_industry VARCHAR(255)
#         )
#     ''')

#     sql = '''INSERT INTO ratings (name_of_issuer, sub_type, instrument_type, amount, rating, industry_name, basic_industry)
#              VALUES (%s, %s, %s, %s, %s, %s, %s)'''

#     cursor.executemany(sql, data)
#     db.commit()
#     cursor.close()
#     db.close()

# # Step 4: Fetch and display data from MySQL
# def fetch_and_display_data():
#     db = mysql.connector.connect(
#         host="127.0.0.1",
#         user="root",
#         password="jaygajjar",
#         database="care_ratings"
#     )
#     cursor = db.cursor()

#     cursor.execute('SELECT * FROM ratings')
#     rows = cursor.fetchall()

#     print("ID | Name of Issuer | Sub Type | Instrument Type | Amount | Rating | Industry Name | Basic Industry")
#     print("--------------------------------------------------------------------------------------------")
#     table = []
#     for row in rows:
#         table.append(row)

#     print(tabulate(table, headers=["ID", "Name of Issuer", "Sub Type", "Instrument Type", "Amount", "Rating", "Industry Name", "Basic Industry"], tablefmt="grid"))

#     cursor.close()
#     db.close()

# if __name__ == "__main__":
#     pdf_path = 'pdffile.pdf'  # Update this to the correct path if needed
#     start_page = 2
#     end_page = 854
#     text = extract_text_from_pdf(pdf_path, start_page, end_page)
#     data = process_text(text)
#     if data:  # Only insert data if it's non-empty
#         insert_data_to_mysql(data)
#         fetch_and_display_data()
#     else:
#         print("No data to insert.")



import json
import mysql.connector
from tabulate import tabulate

# Step 1: Load data from JSON file
def load_data_from_json(json_path):
    with open(json_path, 'r') as file:
        data = json.load(file)
    return data

# Step 2: Insert data into MySQL
def insert_data_to_mysql(data):
    if not data:
        print("No data to insert.")
        return

    db = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="jaygajjar",
        database="care_ratings"
    )
    cursor = db.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ratings (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name_of_issuer VARCHAR(255),
            sub_type VARCHAR(255),
            instrument_type VARCHAR(255),
            amount DECIMAL(20, 2),
            rating VARCHAR(50),
            industry_name VARCHAR(255),
            basic_industry VARCHAR(255)
        )
    ''')

    try:
        sql = '''INSERT INTO ratings (name_of_issuer, sub_type, instrument_type, amount, rating, industry_name, basic_industry)
                 VALUES (%s, %s, %s, %s, %s, %s, %s)'''

        cursor.executemany(sql, data)
        db.commit()
        print("Data inserted successfully.")
    except Exception as e:
        print(f"Error inserting data: {e}")
        db.rollback()

    cursor.close()
    db.close()


# Step 3: Fetch and display data from MySQL
def fetch_and_display_data():
    db = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="jaygajjar",
        database="care_ratings"
    )
    cursor = db.cursor()

    cursor.execute('SELECT * FROM ratings')
    rows = cursor.fetchall()

    print("ID | Name of Issuer | Sub Type | Instrument Type | Amount | Rating | Industry Name | Basic Industry")
    print("--------------------------------------------------------------------------------------------")
    table = []
    for row in rows:
        table.append(row)

    print(tabulate(table, headers=["ID", "Name of Issuer", "Sub Type", "Instrument Type", "Amount", "Rating", "Industry Name", "Basic Industry"], tablefmt="grid"))

    cursor.close()
    db.close()

if __name__ == "__main__":
    json_path = 'pdffile.json'  
    data = load_data_from_json(json_path)
    if data:  # Only insert data if it's non-empty
        insert_data_to_mysql(data)
        fetch_and_display_data()
    else:
        print("No data to insert.")

