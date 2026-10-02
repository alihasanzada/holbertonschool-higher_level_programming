#!/usr/bin/python3
"""A Flask application that displays products from JSON or CSV files."""
import csv
import json
import os
from flask import Flask, render_template, request

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def read_json_products():
    """Return the list of products stored in products.json."""
    path = os.path.join(BASE_DIR, 'products.json')
    with open(path, 'r') as file:
        return json.load(file)


def read_csv_products():
    """Return the list of products stored in products.csv."""
    path = os.path.join(BASE_DIR, 'products.csv')
    products = []
    with open(path, 'r', newline='') as file:
        for row in csv.DictReader(file):
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
    return products


@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')


@app.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Render the contact page."""
    return render_template('contact.html')


@app.route('/items')
def items():
    """Read the items from items.json and render them as a list."""
    path = os.path.join(BASE_DIR, 'items.json')
    try:
        with open(path, 'r') as file:
            item_list = json.load(file).get('items', [])
    except (OSError, ValueError):
        item_list = []
    return render_template('items.html', items=item_list)


@app.route('/products')
def products():
    """Display the products of the requested source, optionally by id."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ('json', 'csv'):
        return render_template('product_display.html', error='Wrong source')

    try:
        if source == 'json':
            data = read_json_products()
        else:
            data = read_csv_products()
    except (OSError, ValueError, KeyError):
        return render_template('product_display.html',
                               error='Could not read the data file')

    if product_id:
        try:
            wanted = int(product_id)
        except ValueError:
            wanted = None
        data = [item for item in data if item.get('id') == wanted]
        if not data:
            return render_template('product_display.html',
                                   error='Product not found')

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
