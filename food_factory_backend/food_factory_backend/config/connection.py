from recruit import settings
import mysql.connector
from mysql.connector import Error

def get_conn():
    """
    Establishes a connection to the MySQL database using Django settings.
    Returns:
        connection: A MySQL connection object if successful, else None.
    """
    connection = None
    try:
        db_settings = settings.DATABASES['default']
        connection = mysql.connector.connect(
            host=db_settings['HOST'],
            user=db_settings['USER'],
            password=db_settings['PASSWORD'],
            database=db_settings['NAME'],
            port=db_settings['PORT']
        )
        if connection.is_connected():
            print("Custom MySQL connection established successfully!")
        return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None

def close_conn(connection):
    """
    Closes the given MySQL database connection.
    Args:
        connection: The MySQL connection object to be closed.
    """
    try:
        if connection and connection.is_connected():
            connection.close()
            print("Custom MySQL connection closed successfully.")
    except Error as e:
        print(f"Error while closing the connection: {e}")