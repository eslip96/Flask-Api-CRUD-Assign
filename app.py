from flask import Flask

from routes.products_routes import product 

app = Flask(__name__)

app.register_blueprint(product)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8086')