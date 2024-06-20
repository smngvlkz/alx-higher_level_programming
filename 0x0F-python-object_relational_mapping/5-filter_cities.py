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

    # Execute the SQL query to fetch cities of the given state
    query = """
        SELECT GROUP_CONCAT(DISTINCT cities.name ORDER BY cities.id SEPARATOR ', ')
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
    """
    cursor.execute(query, (state_name,))

    # Fetch the result of the query
    cities_result = cursor.fetchone()[0]

    # Print the cities or indicate no cities found for the state
    if cities_result:
        print(cities_result)
    else:
        print("No cities found for the state:", state_name)

    # Close the cursor and database connection
    cursor.close()
    db.close()
