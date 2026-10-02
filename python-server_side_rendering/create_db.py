#!/usr/bin/python3
"""Create and populate the products.db SQLite database."""
import os
import sqlite3


def create_database():
    """Create the Products table and insert the two example products."""
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        'products.db')
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    cursor.execute('''
        INSERT OR IGNORE INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')
    conn.commit()
    conn.close()


if __name__ == '__main__':
    create_database()
