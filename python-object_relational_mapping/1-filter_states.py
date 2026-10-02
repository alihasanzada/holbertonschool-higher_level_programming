#!/usr/bin/python3
"""Lists all states with a name starting with N.

This module connects to a MySQL server and prints every state of the
given database whose name begins with an upper case N, sorted by id.
"""
import MySQLdb
import sys


def list_states(username, password, db_name):
    """Print all states whose name starts with an upper N, sorted by id."""
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' "
                "ORDER BY states.id ASC")
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    list_states(sys.argv[1], sys.argv[2], sys.argv[3])
