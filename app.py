import mysql.connector
from mysql.connector import Error


def fetch_data(query):
    try:
        connection = mysql.connector.connect(
            host="localhost", database="workout_tracker", user="root", passwd="0321"
        )

        if connection.is_connected():
            print("Connected to database")
            cursor = connection.cursor()
            cursor.execute(query)
            records = cursor.fetchall()
            print("Total number of rows", cursor.rowcount)
            print("Print each record")

            for row in records:
                print(row)

    except Error as e:
        print("Error while connecting", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


fetch_data("SELECT * FROM workouts")
