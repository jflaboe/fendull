from flask import Flask, request
from data_interface import *
import json

app = Flask(__name__)

@app.route('/challenges', methods=['GET', 'POST'])
def challenges():
    
    data = DataInterface()
    
    return {"data": data.list_challenges()}

@app.route('/addchallenge', methods=['GET'])
def add_challenge():

    name = request.args.get("name")
    points = request.args.get("points")
    path = request.args.get("path")

    data = DataInterface()
    data.add_challenge(name, points, path)
    return "success"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001)