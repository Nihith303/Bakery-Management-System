import mysql.connector

keys = ('localhost', 'root', 'Nihith&*3003', 'bakery')
class data_entry:
    def insert_Orders(self, data, price):
        try:
            conn = mysql.connector.connect(
                host=keys[0],
                user=keys[1],
                password=keys[2],
                database=keys[3]
            )
            cursor = conn.cursor()
            insert_query = "INSERT INTO Orders VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(insert_query, data)
            insert_query2 = "INSERT INTO CashIn (id, price) VALUES (%s, %s)"
            cursor.execute(insert_query2, (data[0], price))
            conn.commit()
            print("Data inserted successfully!")
            return_var =  True
        except mysql.connector.Error as error:
            if error.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
                print("Access denied error: Check your username and password.")
            elif error.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist.")
            elif error.errno == mysql.connector.errorcode.ER_DUP_ENTRY:
                print("Duplicate entry error: This record already exists.")
            else:
                print(f"MySQL Error: {error}")
            return_var =  False
        finally:
            if 'cursor' in locals() and cursor is not None:
                cursor.close()
            if 'conn' in locals() and conn is not None:
                conn.close()
        return return_var

