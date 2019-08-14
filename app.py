from flask import Flask, jsonify
from products import products

app = Flask(__name__)


@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "pong"})


@app.route("/products", methods=['GET'])
def getProducts():
    return jsonify({"products":[products]})

@app.route("/product/<string:product_name>", methods=['GET'])
def getProduct(product_name):
    for product in products:
        if product["name"]==product_name:
            print('se encontro')
            return jsonify({"product":[product]})
    return jsonify({"message":"no se encontro"})


if __name__ == '__main__':
    app.run(debug=True, port=8000)
