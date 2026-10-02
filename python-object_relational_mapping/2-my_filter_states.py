#!/usr/bin/python3
"""Displays the states matching a name given as argument.

This module connects to a MySQL server and prints every row of the
states table whose name matches the argument, sorted by id. The query
is built with str.format, so it is open to SQL injection on purpose.
"""
import MySQLdb
import sys


def filter_states(username, password, db_name, state_name):
    """Print the states whose name matches state_name, sorted by id."""
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' "
                "ORDER BY states.id ASC".format(state_name))
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    filter_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
