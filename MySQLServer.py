
import mysql.connector
from mysql.connector import errorcode

# --- Configuration ---
# IMPORTANT: Update these with your actual MySQL server credentials
DB_HOST = "localhost"
DB_USER = "root"      # e.g., 'root' or 'my_user'
DB_PASSWORD = "Dinar @2025"  # Your MySQL password
DATABASE_NAME = "alx_book_store"

def create_database():
    """
    Connects to the MySQL server and creates the specified database 
    using IF NOT EXISTS to prevent failure.
    """
    db_connection = None
    cursor = None
    
    try:
        # 1. Establish connection to the MySQL server (without specifying a database)
        db_connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD
        )

        # Ensure the connection was successful
        if db_connection.is_connected():
            cursor = db_connection.cursor()
            
            # Use the CREATE DATABASE IF NOT EXISTS statement
            create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
            
            # 2. Execute the query
            cursor.execute(create_db_query)
            
            # 3. Print success message (required)
            print(f"Database '{DATABASE_NAME}' created successfully!")
            
    except mysql.connector.Error as err:
        # Handle specific connection errors (Access Denied, etc.)
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Failed to connect to DB. Check your MySQL username and password.")
        elif err.errno == errorcode.CR_CONN_HOST_ERROR:
            print(f"Error: Failed to connect to DB. MySQL server is not running or host '{DB_HOST}' is incorrect.")
        else:
            # Handle any other execution errors
            print("Error: Failed to execute query.")
            print(f"MySQL Error: {err}")
        
    finally:
        # 4. Handle close of DB connection and cursor
        if cursor:
            cursor.close()
        if db_connection and db_connection.is_connected():
            db_connection.close()
            # print("DB connection closed.") # Optional confirmation

if __name__ == "__main__":
    create_database()