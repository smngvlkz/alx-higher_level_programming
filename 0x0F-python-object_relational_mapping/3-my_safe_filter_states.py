#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and state name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL database
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL query to fetch states matching the provided name, safely
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    # Fetch all the results of the query
    states = cursor.fetchall()

    # Print each state
    for state in states:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()
