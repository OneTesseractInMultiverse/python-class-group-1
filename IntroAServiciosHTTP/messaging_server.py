import os
from flask import Flask, jsonify, request
import requests


app = Flask("MessagingServer")
app.debug = True

subscribers = []

def is_registered(ip, subscribers):
    if ip in subscribers:
        return True
    return False

def get_message_endpoint_for(ip):
    return "http://{}:5000/api/v1/message".format(ip)

def send_message_to_subscriber(subscriber_ip, message, app):
    try:
        url = get_message_endpoint_for(subscriber_ip)
        request.put(url, json={"msg": message})
        app.logger.debug(response.status_code)
        return True
    except Exception as e:
        app.logger.error(e)
        app.logger.error(e.message)
        return False

def broadcast_message_to_subscribers(subscribers, app, message):
    for subscriber_ip in subscribers:
        result = send_message_to_subscriber(subscriber_ip, message, app)
        app.logger.debug("Message to {} sent: {}".format(subscriber_ip, result))
    return len(subscribers)

@app.route("/api/v1/subscriber", methods=["GET"])
def get_subscribers():
    return jsonify(subscribers)


@app.route("/api/v1/message", methods=["PUT"])
def put_message():
    # esto es una validación para garantizar que los datos vienen en json que es 
    # lo que este servidor sabe interpretar.
    if not request.is_json:
        return jsonify({
            "msg": "Only json is supported in this api"
        }), 400
    
    # Si llegamos acá es porque los datos sí son JSON
    datos = request.get_json()

    if "msg" not in datos:
        return jsonify({
            "msg": "msg is not present"
        }), 400

    app.logger.debug(datos["msg"])

    return jsonify({
        "msj": "OK"
    }), 200

@app.route("/api/v1/message", methods=["POST"])
def post_message():

    if not request.is_json:
        return jsonify({
            "msg": "Only json is supported in this api"
        }), 400
    
    # Si llegamos acá es porque los datos sí son JSON
    datos = request.get_json()

    if "msg" not in datos:
        return jsonify({
            "msg": "msg is not present"
        }), 400

    messages_sent = broadcast_message_to_subscribers(subscribers, app, datos["msg"])
    return jsonify({
        "msg": "{} messages broadcasted".format(messages_sent)
    }), 200

# POST /api/v1/subscriber
@app.route("/api/v1/subscriber", methods=["POST"])
def post_subscriber():

    # esto es una validación para garantizar que los datos vienen en json que es 
    # lo que este servidor sabe interpretar.
    if not request.is_json:
        return jsonify({
            "msg": "Only json is supported in this api"
        }), 400
    
    # Si llegamos acá es porque los datos sí son JSON
    datos = request.get_json()

    if not "ip" in datos:
        return jsonify({
            "msg": "Ip is a required field"
        }), 400

    if is_registered(datos["ip"], subscribers):
        return jsonify({
            "msg": "Ip is already reguistered"
        }), 400

    subscribers.append(datos["ip"])
    return jsonify({
        "msg": "IP: {} was registered".format(datos["ip"])
    }), 201

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)