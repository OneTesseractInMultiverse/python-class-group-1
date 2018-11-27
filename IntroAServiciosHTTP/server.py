"""
Antes de ejecutar este programa, se debe instalar flask por medio del comando:
pip install flask
"""
import os
from flask import Flask, jsonify


app = Flask("EvilApi")

@app.route('/')
def get_root_resource():
    return 'This is a root resource'

@app.route('/api/v1/person', methods=["GET"])
def get_person():
    return jsonify({
        "name": "John", 
        "last_name": "Smith"
    }), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)