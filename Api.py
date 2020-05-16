import flask
from flask import jsonify, request

from services import StuffService

app = flask.Flask(__name__)
app.config["DEBUG"] = True

_stuffService = StuffService.StuffService()

@app.route('/api', methods=['GET'])
def home():
    return "<h1>My first Flask API.</p>"

@app.route('/api/stuff/all', methods=['GET'])
def api_stuff_all():
    stuff = _stuffService.get_all()
    return jsonify(stuff)

app.run()
