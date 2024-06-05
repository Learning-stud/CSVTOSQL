

# Connect to MySQL database
# mydb = mysql.connector.connect(
#   host="127.0.0.1",
#   user="root",
#   password="jaygajjar",
#   database="RatingsDB"
# )
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
    issuer VARCHAR(255),
    sub_type VARCHAR(255),
    instrument_type VARCHAR(255),
    amount DECIMAL(15, 2),
    rating VARCHAR(50),
    industry_name VARCHAR(255),
    basic_industry VARCHAR(255)
)
"""
cursor.execute(create_table_query)

# Insert data into MySQL table
# Insert data into MySQL table
for index, row in df.iterrows():
    insert_query = """
    INSERT INTO Ratings (issuer, sub_type, instrument_type, amount, rating, industry_name, basic_industry)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(insert_query, tuple(row))
    conn.commit()


# Close connection
cursor.close()
conn.close()
