#!/usr/bin/python3

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Extract command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    # Create engine to connect to MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, dbname),
                           pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query the State object with the name passed as argument
    state = session.query(State).filter(State.name == state_name).first()

    # Print the results
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")

    # Close the session
    session.close()
