from flask import jsonify, request

from data import product_records

def read_products_by_id(product_id):
    for product in product_records:
        if product['product_id'] == int(product_id):
            return jsonify({"message": "product found!", "results": product}), 200
    return jsonify({"message": f'product with id {product_id} not found.'}), 400

def get_all_products():
    return jsonify({'message': 'products found', 'results': product_records}), 200


def get_active_products():
    active_products = []

    for product in product_records:
        if product.get('active', False):
            active_products.append(product)

    if active_products:
        return jsonify({'message': 'here are the listed active products', 'active_products': active_products})
    else:
        return jsonify({'message': 'no active products found'})
        


def add_product():
    data = request.form if request.form else request.json
    product = {}

    product['product_id'] = data['product_id']
    product['name'] = data['name']
    product['description'] = data['description']
    product['price'] = data['price']
    product['active'] = data['active']

    product_records.append(product)

    return jsonify({'message': 'product added', 'results': product}), 201

def edit_product(product_id):
    data = request.form if request.form else request.json

    product = {}

    for record in product_records:
        if record['product_id'] == int(product_id):
            product = record
            product['name'] = data.get('name', product['name'])   
            product['description'] = data.get('description', product['description'])
            product['price'] = data.get('price', product['price'])
            product['active'] = data.get('active', product['active'])

            return jsonify({'message': 'product updated', 'results': product}), 200      

def delete_product(product_id):
    for product in product_records:
        if product['product_id'] == int(product_id):
            product_records.remove(product)
            return jsonify({'message': f'product {product_id} has been removed'}), 200