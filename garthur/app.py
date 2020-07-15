from flask import Flask
from flask import render_template
from pymongo import MongoClient
import json
from bson import json_util

app = Flask(__name__)

ATLAS_CONNECTION = 'mongodb+srv://arthurga:test@arthurga-mongo-kraha.mongodb.net/thesis?retryWrites=true&w=majority'

FIELDS = {'DATE_REPORTED': True, 'OFFENSE': True, 'LOCATION': True, 'THEFT_CODE': True, 'DAYOFWEEK': True,
          'RPT_AREA': True, 'CPD_NEIGHBORHOOD': True, 'SNA_NEIGHBORHOOD': True, 'WEAPONS': True, 'ADDRESS_X': True,
          'LONGITUDE_X': True, 'LATITUDE_X': True, 'UCR_GROUP': True, 'ZIP': True, '_id': False}


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/thesis/analysis')
def thesis_project():
    client = MongoClient(host=ATLAS_CONNECTION)
    collection = client.thesis.CrimeData
    docs = collection.find(projection=FIELDS, limit=10)
    json_projects = []
    for doc in docs:
        json_projects.append(doc)
    json_projects = json.dumps(json_projects, default=json_util.default)
    client.close()
    return json_projects


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
