#!/usr/bin/python3
"""Adds a city and its associated state in the database"""
import sys
from relationship_state import State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, City

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = State(name="California")
    city = City(name="San Francisco", state=state)

    session.add(state)
    session.add(city)
    session.commit()
