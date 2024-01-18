from flask import Flask,jsonify, request

from data import product_records

def read_products_by_id(id):
    for product in product_records:
        if product['product_id'] == int(id):
            return jsonify({"message": "product found!", "results": product}), 200
    return jsonify({"message": f'product with id {id} not found.'}), 400

def add_product():
    data = request.form if request.form else request.json
    product = {}

    product['product_id'] = data['product_id']
    product['name'] = data['name']
    product['description'] = data['description']
    product['price'] = data['price']

    product_records.append(product)

    return jsonify({'message': 'product added', 'results': product})