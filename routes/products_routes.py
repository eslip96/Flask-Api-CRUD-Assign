from flask import Blueprint

from controllers import products_controllers

product = Blueprint('product', '__name__')

@product.route('/products/get/<product_id>', methods=["GET"])
def read_products_by_id(product_id):
    return products_controllers.read_products_by_id(product_id)


@product.route('/products', methods=["GET"])
def get_all_products():
    return products_controllers.get_all_products()


@product.route('/products/get/active', methods=["GET"])
def get_active_products():
    return products_controllers.get_active_products()


@product.route('/products/<product_id>', methods=['PUT'])
def edit_product(product_id):
    return products_controllers.edit_product(product_id)


@product.route('/products/', methods=['POST'])
def add_product():
    return products_controllers.add_product()

@product.route('/product/delete/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    return products_controllers.delete_product(product_id)