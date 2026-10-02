#!/usr/bin/python3
"""Lists all State objects and their City objects of a database.

This module uses SQLAlchemy to print every state of the given MySQL
database followed by the cities of its cities relationship.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import Session
from relationship_state import State
# City must be imported so that SQLAlchemy can resolve the relationship.
from relationship_city import City


def list_states_cities(username, password, db_name):
    """Print all states and their cities, sorted by state and city id."""
    url = URL.create("mysql+mysqldb", username=username, password=password,
                     host="localhost", port=3306, database=db_name)
    engine = create_engine(url, pool_pre_ping=True)
    session = Session(engine)
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
        for city in sorted(state.cities, key=lambda c: c.id):
            print("\t{}: {}".format(city.id, city.name))
    session.close()


if __name__ == "__main__":
    list_states_cities(sys.argv[1], sys.argv[2], sys.argv[3])
