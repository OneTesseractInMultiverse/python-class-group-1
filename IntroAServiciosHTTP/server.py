"""
Antes de ejecutar este programa, se debe instalar flask por medio del comando:
pip install flask
"""
import os
from flask import Flask, jsonify, request


app = Flask("EvilApi")
app.debug = True

persons = []
subscribers = []



def id_exists(id, persons):
    app.logger.debug("id_exists was called")
    app.logger.debug(id)
    app.logger.debug(persons)
    for person in persons:
        if person["id"] == id:
            return True
    return False

def post_subscriber():
    if not request.is_json:
        return jsonify({
            "msg": "Only json is supported in this api"
        }), 400

    datos = request.get_json()

    if "ip" not in datos:
        return jsonify({
            "msg": "An id is required"
        }), 400

    subscribers.append(datos["ip"])
    return jsonify({"msg": "todo salio bien"}), 200

@app.route('/')
def get_root_resource():
    return 'This is a root resource'

@app.route('/api/v1/person', methods=["POST"])
def post_person():
    # esto es una validación para garantizar que los datos vienen en json que es 
    # lo que este servidor sabe interpretar.
    if not request.is_json:
        return jsonify({
            "msg": "Only json is supported in this api"
        }), 400
    
    # Si llegamos acá es porque los datos sí son JSON
    datos = request.get_json()

    # Para poder crear una persona (recurso) es mandatorio 
    # que tenga un id único
    if "id" not in datos:
        return jsonify({
            "msg": "An id is required"
        }), 400

    if id_exists(datos["id"], persons):
        return jsonify({
            "msg": "The provided id is already in use"
        }), 400

    persons.append(datos)

    return jsonify({
        "msg": "Person created"
    }), 201

@app.route('/api/v1/person', methods=["GET"])
def get_person():
    return jsonify(persons), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)