import pandas as pd
import mysql.connector

# Load CSV into a DataFrame
df = pd.read_csv("301-600.csv")

# Connect to MySQL
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="jaygajjar",
    database="RatingsDB"
)
cursor = conn.cursor()

# Define the MySQL table schema
create_table_query = """
CREATE TABLE IF NOT EXISTS Ratings (
    NAME_OF_ISSUER VARCHAR(255),
    INSTRUMENT_TYPE VARCHAR(255),
    AMOUNT DECIMAL(15, 2),
    RATING VARCHAR(50),
    INDUSTRY_NAME VARCHAR(255),
    NSEINDUSTRY VARCHAR(255)
)
"""
cursor.execute(create_table_query)

# Insert data into MySQL table
for index, row in df.iterrows():
    insert_query = """
    INSERT INTO Ratings (NAME_OF_ISSUER,  INSTRUMENT_TYPE, AMOUNT, RATING, INDUSTRY_NAME, NSEINDUSTRY)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    # Ignore the first column 'NAME_OF_ISSUER' while inserting data into MySQL
    cursor.execute(insert_query, tuple(row[1:]))
    conn.commit()

# Close connection
cursor.close()
conn.close()
