#!/usr/bin/python3
"""Lists all State objects and their City objects of a database.

This module uses SQLAlchemy to print every state of the given MySQL
database followed by its cities, using only one query to the database.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, contains_eager
from relationship_state import Base, State
from relationship_city import City


def list_states_cities(username, password, db_name):
    """Print all states and their cities, sorted by state and city id."""
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username, password, db_name),
        pool_pre_ping=True)
    session = Session(engine)
    states = (session.query(State)
              .outerjoin(State.cities)
              .options(contains_eager(State.cities))
              .order_by(State.id, City.id)
              .all())
    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))
    session.close()


if __name__ == "__main__":
    list_states_cities(sys.argv[1], sys.argv[2], sys.argv[3])
