import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Nihith&*3003",
        database="college"
    )

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Example data to insert
    data_to_insert = ("John", 92827, 30, 30, 30)

    # SQL query to insert data
    insert_query = "INSERT INTO marks VALUES (%s, %s, %s, %s, %s)"

    # Execute the query
    cursor.execute(insert_query, data_to_insert)

    # Commit changes to the database
    conn.commit()

    print("Data inserted successfully!")

except mysql.connector.Error as error:
    # Handle specific types of MySQL errors
    if error.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
        print("Access denied error: Check your username and password.")
    elif error.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist.")
    elif error.errno == mysql.connector.errorcode.ER_DUP_ENTRY:
        print("Duplicate entry error: This record already exists.")
    else:
        print(f"MySQL Error: {error}")

finally:
    # Close cursor and connection
    if 'cursor' in locals() and cursor is not None:
        cursor.close()
    if 'conn' in locals() and conn is not None:
        conn.close()
