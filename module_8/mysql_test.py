/*
    
    Author: Dylan Cooper
    Date: 7-20-2023
    Description: mysql test connection module 8.2
*/
import mysql.connector

def test_database_connection():
    config = {
        "user": "your_database_user",
        "password": "PassWord",
        "host": "test",
        "database": "pytest",
        "raise_on_warnings": True
    }

    try:
        # Establishing a connection to mysql
        db = mysql.connector.connect(**config)
        if db.is_connected():
            print("Connected to the pytest database!")
            print("Hello, are you there?")

    except mysql.connector.Error as error:
        print(f"Error while connecting to MySQL: {error}")

    finally:
        # Closing the connection to the database
        if 'db' in locals() and db.is_connected():
            db.close()
            print("Connection to MySQL database closed!")

if __name__ == "__main__":
    test_database_connection()
