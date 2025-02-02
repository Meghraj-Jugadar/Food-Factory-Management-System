from constants.queries import USER_INSERT_QUERY 

def insert_user(db_connection, data):
    """ Insert a new user into the database.
    Args:
        db_connection: The active database connection.
        data (dict): A dictionary containing user data.
            Required keys: 'username', 'email', 'password', 'role', 'is_delete'.
    Returns:
        bool: True if the user was successfully inserted, False otherwise."""

    try:
        cursor = db_connection.cursor()
        print("Data - ", data)
        cursor.execute(USER_INSERT_QUERY, (
            data.get('username'),
            data.get('email'),
            data.get('password'),
            data.get('role'),
            data.get('is_delete', 0)  
        ))

        # Commit the transaction
        db_connection.commit()
        return True
    except Exception as e:
        print(f"Error inserting user: {str(e)}")
        return False


def fetchall_users(db_connection):
    try:
        cursor = db_connection.cursor()
        data = cursor.execute(FETCH_ALL_USERS_QUERY)
        db_connection.commit()
        return data
    except Exception as e:
        print(f"Error fetching users: {str(e)}")
        return e
    