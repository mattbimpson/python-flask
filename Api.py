import flask
from flask import jsonify, request
from flask_cors import CORS, cross_origin

from services import StuffService

app = flask.Flask(__name__)
cors = CORS(app)
app.config["DEBUG"] = True
app.config['CORS_HEADERS'] = 'Content-Type'

_stuffService = StuffService.StuffService()

@app.route('/api', methods=['GET'])
@cross_origin()
def home():
    return "<h1>My first Flask API.</p>"

@app.route('/api/stuff/all', methods=['GET'])
@cross_origin()
def api_stuff_all():
    stuff = _stuffService.get_all()
    return jsonify(stuff)

app.run()
