#!/usr/bin/python3
"""Lists all cities of a database together with their state.

This module connects to a MySQL server and prints every city of the
given database with its state name, sorted by cities.id ascending.
"""
import MySQLdb
import sys


def list_cities(username, password, db_name):
    """Print every city with its state name, sorted by cities.id."""
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name "
                "FROM cities "
                "INNER JOIN states ON cities.state_id = states.id "
                "ORDER BY cities.id ASC")
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    list_cities(sys.argv[1], sys.argv[2], sys.argv[3])
