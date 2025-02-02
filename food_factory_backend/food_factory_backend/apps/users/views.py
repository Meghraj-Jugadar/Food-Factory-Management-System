from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from .models import User
from config.connection import get_conn, close_conn


class UserInsertView(APIView):
    def post(self, request):
        db_connection = None
        try:
            # Start the database connection
            db_connection = get_conn()
            if not db_connection:
                return Response({"error": "Failed to connect to the database"}, status=500)
            
            # Extract data from the request body
            data = request.data
            username = data.get('username')
            email = data.get('email')
            password = data.get('password')
            role = data.get('role')
            is_delete = data.get('is_delete', 0)  # Default to 0 if not provided

            # Ensure that all necessary fields are provided
            if not all([username, email, password, role, is_delete]):
                return Response({"error": "Missing required fields."}, status=400)

            # Prepare the SQL query
            query = """
                INSERT INTO users (username, email, password, role, is_delete)
                VALUES (%s, %s, %s, %s, %s, %s);
            """
            cursor = db_connection.cursor()
            cursor.execute(query, (username, email, password, role, is_delete))

            # Commit the transaction
            db_connection.commit()

            # Return a success response
            return Response({"message": "Candidate created successfully."}, status=201)

        except Exception as e:
            # Handle any exceptions and return a 500 error response
            return Response({"error": str(e)}, status=500)

        finally:
            # Ensure the connection is closed
            if db_connection:
                close_conn(db_connection)


