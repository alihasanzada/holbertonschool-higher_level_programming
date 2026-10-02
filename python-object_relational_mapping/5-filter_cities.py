#!/usr/bin/python3
"""Lists all cities of the state given as argument.

This module connects to a MySQL server and prints the names of all the
cities of the given state on one line, sorted by cities.id ascending.
The query is parameterized, so it is safe from SQL injection.
"""
import MySQLdb
import sys


def filter_cities(username, password, db_name, state_name):
    """Print the cities of state_name on one line, sorted by cities.id."""
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities "
                "INNER JOIN states ON cities.state_id = states.id "
                "WHERE states.name = %s "
                "ORDER BY cities.id ASC", (state_name,))
    print(", ".join(row[0] for row in cur.fetchall()))
    cur.close()
    db.close()


if __name__ == "__main__":
    filter_cities(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
