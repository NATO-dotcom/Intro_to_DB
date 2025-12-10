def create_database():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Dinar @2025"
        )
        if connection.is_connected():
            print("Connected!")
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS intro_db;")
            print("Database created.")

    except mysql.connector.Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if connection is not None and connection.is_connected():
            connection.close()
