from flask import Flask, jsonify, request
from products import products
import json
app = Flask(__name__)


@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "pong"})


@app.route("/products", methods=['GET'])
def getProducts():
    return jsonify({"products":[products]})

@app.route("/products", methods=['POST'])
def createProduct():
    nuevoproducto = json.dumps(request.json)
    nuevoproducto = json.loads(nuevoproducto)
    print(nuevoproducto)
    products.append(nuevoproducto)
    return jsonify({"message":"producto agregado",
                    "producto":[nuevoproducto]})

@app.route("/product/<string:product_name>", methods=['GET'])
def getProduct(product_name):
    for product in products:
        if product["name"]==product_name:
            return jsonify({"product":[product]})
    return jsonify({"message":"no se encontro"})

@app.route("/product/<string:product_name>", methods=['PUT'])
def editProduct(product_name):
        productf  = [product for product in products if product["name"]==product_name]
        editproducto = request.json
        if(len(productf)>0):
            productf[0]['name'] = editproducto['name']
            productf[0]['price'] = editproducto['price']
            productf[0]['quantity'] = editproducto['quantity']
            print("el nuevo valor de product es: ",productf)
            return jsonify({"message": "producto editado",
                            "producto": [productf]})
        return jsonify({"message":"no se encontro"})

@app.route("/product/<string:product_name>", methods=['DELETE'])
def deleteProduct(product_name):
    productf = [product for product in products if product["name"] == product_name]
    if (len(productf) > 0):
        products.remove(productf[0])
        return jsonify({"message": "producto eliminado",
                        "producto": [productf]})
    return jsonify({"message": "no se encontro"})
if __name__ == '__main__':
    app.run(debug=True, port=8000)
