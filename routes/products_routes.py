from flask import Blueprint,request,jsonify

from controllers import products_controllers

product = Blueprint('product', '__name__')

@product.route('/products/get/<id>', methods=["GET"])
def read_products_by_id(id):
    return products_controllers.read_products_by_id(id)

@product.route('/products<id>', methods=['PUT'])
def edit_product():
    product = request.form if request.form else request.json
    return products_controllers.read_products_by_id(id)

@product.route('/products/<', methods=['POST'])
def add_product():

