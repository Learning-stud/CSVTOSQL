# # # import fitz  # PyMuPDF
# # # import re
# # # import mysql.connector

# # # # Open the PDF file
# # # pdf_document = "pdffile.pdf"
# # # doc = fitz.open(pdf_document)

# # # # Function to extract and parse data from each page
# # # def extract_data_from_pdf(doc):
# # #     data = []
# # #     for page_num in range(len(doc)):
# # #         page = doc.load_page(page_num)
# # #         text = page.get_text("text")

# # #         print("Extracted text from page", page_num + 1, ":", text)

# # #         # Find all rows of data
# # #         matches = re.findall(r'(\d+)\s+([\w\s]+)\s+([\w\s]+)\s+([\w\s]+)\s+([\d,\.]+)\s+([\w\s\+;\-]+)\s+([\w\s]+)\s+([\w\s\+;\-]+)', text)

# # #         print("Matches found on page", page_num + 1, ":", matches)
# # #         for match in matches:
# # #             print("Amount:", match[4])  # Print 'amount' data
# # #             row = {
# # #                 'serial': match[0],
# # #                 'issuer': match[1].strip()[:100],  # Truncate issuer to 100 characters
# # #                 'sub_type': match[2].strip(),
# # #                 'instrument_type': match[3].strip(),
# # #                 'amount': match[4].replace(',', ''),
# # #                 'rating': match[5].strip()[:50],  # Truncate rating to 50 characters
# # #                 'industry_name': match[6].strip(),
# # #                 'basic_industry': match[7].strip()
# # #             }
# # #             data.append(row)
# # #     return data

# # # data = extract_data_from_pdf(doc)
# # # print("Extracted data:", data)  # Print extracted data

# # # # Database connection parameters
# # # db_config = {
# # #     'user': 'root',
# # #     'password': 'jaygajjar',
# # #     'host': '127.0.0.1',
# # #     'database': 'pdf_database'  # Replace with your database name
# # # }

# # # # Connect to the database
# # # cnx = mysql.connector.connect(**db_config)
# # # cursor = cnx.cursor()

# # # # Insert data into MySQL
# # # add_data = ("INSERT INTO ratings "
# # #             "(serial, issuer, sub_type, instrument_type, amount, rating, industry_name, basic_industry) "
# # #             "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")

# # # for row in data:
# # #     data_row = (
# # #         row['serial'],
# # #         row['issuer'],  # Truncated issuer already
# # #         row['sub_type'],
# # #         row['instrument_type'],
# # #         row['amount'],
# # #         row['rating'],
# # #         row['industry_name'],
# # #         row['basic_industry']
# # #     )
# # #     cursor.execute(add_data, data_row)

# # # # Commit and close the connection
# # # cnx.commit()
# # # cursor.close()
# # # cnx.close()

# # # print("Data has been successfully inserted into the database.")

# # # # import fitz  # PyMuPDF
# # # # import re
# # # # import mysql.connector

# # # # # Open the PDF file
# # # # pdf_document = "601-855.pdf"
# # # # doc = fitz.open(pdf_document)

# # # # # Function to extract and parse data from each page
# # # # def extract_data_from_pdf(doc):
# # # #     data = []
# # # #     for page_num in range(len(doc)):
# # # #         page = doc.load_page(page_num)
# # # #         text = page.get_text("text")

# # # #         # Find all rows of data
# # # #         matches = re.findall(r'(\d+)\s+([\w\s]+)\s+([\w\s]+)\s+([\w\s]+)\s+([\d,\.]+)\s+([\w\s\+;\-]+)\s+([\w\s]+)\s+([\w\s\+;\-]+)', text)

# # # #         for match in matches:
# # # #             row = {
# # # #                 'serial': match[0],
# # # #                 'issuer': match[1].strip()[:100],  # Truncate issuer to 100 characters
# # # #                 'sub_type': match[2].strip(),
# # # #                 'instrument_type': match[3].strip(),
# # # #                 'amount': match[4].replace(',', ''),
# # # #                 'rating': match[5].strip()[:50],  # Truncate rating to 50 characters
# # # #                 'industry_name': match[6].strip(),
# # # #                 'basic_industry': match[7].strip()
# # # #             }
# # # #             data.append(row)
# # # #     return data

# # # # data = extract_data_from_pdf(doc)

# # # # # Database connection parameters
# # # # db_config = {
# # # #     'user': 'root',
# # # #     'password': 'jaygajjar',
# # # #     'host': '127.0.0.1',
# # # #     'database': 'pdf_database'  # Replace with your database name
# # # # }

# # # # # Connect to the database
# # # # cnx = mysql.connector.connect(**db_config)
# # # # cursor = cnx.cursor()

# # # # # Insert data into MySQL
# # # # add_data = ("INSERT INTO ratings "
# # # #             "(serial, issuer, sub_type, instrument_type, amount, rating, industry_name, basic_industry) "
# # # #             "VALUES (%(serial)s, %(issuer)s, %(sub_type)s, %(instrument_type)s, %(amount)s, %(rating)s, %(industry_name)s, %(basic_industry)s)")

# # # # for row in data:
# # # #     cursor.execute(add_data, row)

# # # # # Commit and close the connection
# # # # cnx.commit()
# # # # cursor.close()
# # # # cnx.close()

# # # # print("Data has been successfully inserted into the database.")


# # import fitz  # PyMuPDF
# # import re
# # import mysql.connector

# # # Open the PDF file
# # pdf_document = "pdffile.pdf"
# # doc = fitz.open(pdf_document)

# # # Function to extract and parse data from each page
# # def extract_data_from_pdf(doc):
# #     data = []
# #     for page_num in range(len(doc)):
# #         page = doc.load_page(page_num)
# #         text = page.get_text("text")

# #         print("Extracted text from page", page_num + 1, ":", text)

# #         # Find all rows of data
# #         matches = re.findall(r'(\d+)\s+([\w\s]+)\s+([\w\s]+)\s+([\w\s]+)\s+([\d,\.]+)\s+([\w\s\+;\-]+)\s+([\w\s]+)\s+([\w\s\+;\-]+)', text)

# #         print("Matches found on page", page_num + 1, ":", matches)
# #         for match in matches:
# #             print("Amount:", match[4])  # Print 'amount' data
# #             row = {
# #                 'serial': match[0],
# #                 'issuer': match[1].strip()[:100],  # Truncate issuer to 100 characters
# #                 'sub_type': match[2].strip(),
# #                 'instrument_type': match[3].strip(),
# #                 'amount': match[4].replace(',', ''),
# #                 'rating': match[5].strip()[:50],  # Truncate rating to 50 characters
# #                 'industry_name': match[6].strip(),
# #                 'basic_industry': match[7].strip()
# #             }
# #             data.append(row)
# #     return data

# # data = extract_data_from_pdf(doc)
# # print("Extracted data:", data)  # Print extracted data

# # # Database connection parameters
# # db_config = {
# #     'user': 'root',
# #     'password': 'jaygajjar',
# #     'host': '127.0.0.1',
# #     'database': 'pdf_database'  # Replace with your database name
# # }

# # # Connect to the database
# # cnx = mysql.connector.connect(**db_config)
# # cursor = cnx.cursor()

# # # Insert data into MySQL
# # add_data = ("INSERT INTO ratings "
# #             "(serial, issuer, sub_type, instrument_type, amount, rating, industry_name, basic_industry) "
# #             "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")

# # for row in data:
# #     data_row = (
# #         row['serial'],
# #         row['issuer'],  # Truncated issuer already
# #         row['sub_type'],
# #         row['instrument_type'],
# #         row['amount'],
# #         row['rating'],
# #         row['industry_name'],
# #         row['basic_industry']
# #     )
# #     cursor.execute(add_data, data_row)

# # # Commit and close the connection
# # cnx.commit()
# # cursor.close()
# # cnx.close()

# # print("Data has been successfully inserted into the database.")


# import fitz  # PyMuPDF
# import re
# import mysql.connector

# # Open the PDF file
# pdf_document = "pdffile.pdf"
# doc = fitz.open(pdf_document)

# # Function to extract and parse data from each page
# def extract_data_from_pdf(doc):
#     data = []
#     for page_num in range(len(doc)):
#         page = doc.load_page(page_num)
#         text = page.get_text("text")

#         print("Extracted text from page", page_num + 1, ":", text)

#         # Find all rows of data
#         matches = re.findall(r'(\d+)\s+([\w\s]+)\s+([\w\s]+)\s+([\w\s]+)\s+([\d,\.]+)\s+([\w\s\+;\-]+)\s+([\w\s]+)\s+([\w\s\+;\-]+)', text)

#         print("Matches found on page", page_num + 1, ":", matches)
#         for match in matches:
#             print("Match:", match)
#             row = {
#                 'serial': match[0],
#                 'issuer': match[1].strip()[:100],  # Truncate issuer to 100 characters
#                 'sub_type': match[2].strip(),
#                 'instrument_type': match[3].strip(),
#                 'amount': match[4].replace(',', ''),
#                 'rating': match[5].strip()[:50],  # Truncate rating to 50 characters
#                 'industry_name': match[6].strip(),
#                 'basic_industry': match[7].strip()
#             }
#             data.append(row)
#     return data

# data = extract_data_from_pdf(doc)
# print("Extracted data:", data)  # Print extracted data

# # Database connection parameters
# db_config = {
#     'user': 'root',
#     'password': 'jaygajjar',
#     'host': '127.0.0.1',
#     'database': 'pdf_database'  # Replace with your database name
# }

# # Connect to the database
# cnx = mysql.connector.connect(**db_config)
# cursor = cnx.cursor()

# # Insert data into MySQL
# add_data = ("INSERT INTO ratings "
#             "(serial, issuer, sub_type, instrument_type, amount, rating, industry_name, basic_industry) "
#             "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")

# for row in data:
#     data_row = (
#         row['serial'],
#         row['issuer'],  # Truncated issuer already
#         row['sub_type'],
#         row['instrument_type'],
#         row['amount'],
#         row['rating'],
#         row['industry_name'],
#         row['basic_industry']
#     )
#     print("Inserting row:", data_row)
#     print("SQL query:", add_data % data_row)
#     try:
#         cursor.execute(add_data, data_row)
#     except mysql.connector.Error as err:
#         print("Error inserting row:", err)

# # Commit and close the connection
# cnx.commit()
# cursor.close()
# cnx.close()

# print("Data has been successfully inserted into the database.")

# import fitz  # PyMuPDF
# import pandas as pd
# import re
# import mysql.connector

# # Open the PDF file
# pdf_document = "pdffile.pdf"
# document = fitz.open(pdf_document)

# # Function to extract text from the PDF
# def extract_text_from_first_page(doc):
#     page = doc.load_page(0)  # Loads the first page
#     text = page.get_text("text")
#     return text

# # Extract text from the first page
# pdf_text = extract_text_from_first_page(document)

# # Extract the tabular data using regular expressions
# def extract_table_data(text):
#     pattern = re.compile(r"(\d+.*\n)+")
#     matches = pattern.findall(text)
#     data = [match.split() for match in matches]
#     return data

# # Process the extracted text
# data = extract_table_data(pdf_text)

# # Convert the processed data into a DataFrame
# columns = ["Name of Issuer", "Subtype Instrument Type", "Amount (Rs.Mn)", "Rating", "Industry Name", "Basic Industry"]
# df = pd.DataFrame(data, columns=columns)

# # Remove any rows where 'Amount (Rs.Mn)' is not a numeric value
# df = df[pd.to_numeric(df['Amount (Rs.Mn)'], errors='coerce').notnull()]

# # Convert 'Amount (Rs.Mn)' to numeric
# df['Amount (Rs.Mn)'] = pd.to_numeric(df['Amount (Rs.Mn)'])

# # MySQL database connection details
# db_config = {
#     'user': 'root',
#     'password': 'jaygajjar',
#     'host': '127.0.0.1',
#     'raise_on_warnings': True
# }

# # Establishing a connection to the database
# connection = mysql.connector.connect(**db_config)
# cursor = connection.cursor()

# # Drop the existing database if it exists
# cursor.execute("DROP DATABASE IF EXISTS PdfDatabase")

# # Create the database
# cursor.execute("CREATE DATABASE PdfDatabase")

# # Creating the table
# create_table_query = """
# CREATE TABLE IF NOT EXISTS PdfDatabase.issuer_ratings (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name_of_issuer VARCHAR(255),
#     subtype_instrument_type VARCHAR(255),
#     amount DECIMAL(15, 2),
#     rating VARCHAR(255),
#     industry_name VARCHAR(255),
#     basic_industry VARCHAR(255)
# )
# """

# cursor.execute(create_table_query)

# # Inserting data into the table
# insert_data_query = """
# INSERT INTO PdfDatabase.issuer_ratings (name_of_issuer, subtype_instrument_type, amount, rating, industry_name, basic_industry)
# VALUES (%s, %s, %s, %s, %s, %s)
# """

# # Converting DataFrame to list of tuples
# data_to_insert = df.to_records(index=False).tolist()

# # Executing the insert query
# cursor.executemany(insert_data_query, data_to_insert)

# # Committing the transaction
# connection.commit()

# # Closing the connection
# cursor.close()
# connection.close()

# print("Data inserted successfully")

import fitz  # PyMuPDF
import pandas as pd
import re
import mysql.connector

# Open the PDF file
pdf_document = "pdffile.pdf"
document = fitz.open(pdf_document)

# Function to extract text from the PDF
def extract_text_from_first_page(doc):
    page = doc.load_page(0)  # Loads the first page
    text = page.get_text("text")
    return text

# Extract text from the first page
pdf_text = extract_text_from_first_page(document)
print("Extracted text from PDF:", pdf_text)

# Extract the tabular data using regular expressions
def extract_table_data(text):
    pattern = re.compile(r"(\d+.*\n)+")
    matches = pattern.findall(text)
    print("Matches found:", matches)
    data = [match.split() for match in matches]
    return data

# Process the extracted text
data = extract_table_data(pdf_text)
print("Processed data:", data)

# Convert the processed data into a DataFrame
columns = ["Name of Issuer", "Subtype Instrument Type", "Amount (Rs.Mn)", "Rating", "Industry Name", "Basic Industry"]
df = pd.DataFrame(data, columns=columns)
print("DataFrame:")
print(df.head())

# Remove any rows where 'Amount (Rs.Mn)' is not a numeric value
df = df[pd.to_numeric(df['Amount (Rs.Mn)'], errors='coerce').notnull()]

# Convert 'Amount (Rs.Mn)' to numeric
df['Amount (Rs.Mn)'] = pd.to_numeric(df['Amount (Rs.Mn)'])

# MySQL database connection details
db_config = {
    'user': 'root',
    'password': 'jaygajjar',
    'host': '127.0.0.1',
    'raise_on_warnings': True
}

# Establishing a connection to the database
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

# Drop the existing database if it exists
cursor.execute("DROP DATABASE IF EXISTS PdfDatabase")

# Create the database
cursor.execute("CREATE DATABASE PdfDatabase")

# Creating the table
create_table_query = """
CREATE TABLE IF NOT EXISTS PdfDatabase.issuer_ratings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name_of_issuer VARCHAR(255),
    subtype_instrument_type VARCHAR(255),
    amount DECIMAL(15, 2),
    rating VARCHAR(255),
    industry_name VARCHAR(255),
    basic_industry VARCHAR(255)
)
"""

cursor.execute(create_table_query)

# Inserting data into the table
insert_data_query = """
INSERT INTO PdfDatabase.issuer_ratings (name_of_issuer, subtype_instrument_type, amount, rating, industry_name, basic_industry)
VALUES (%s, %s, %s, %s, %s, %s)
"""

# Converting DataFrame to list of tuples
data_to_insert = df.to_records(index=False).tolist()
print("Data to insert:", data_to_insert)

# Executing the insert query
cursor.executemany(insert_data_query, data_to_insert)

# Committing the transaction
connection.commit()

# Closing the connection
cursor.close()
connection.close()

print("Data inserted successfully")
