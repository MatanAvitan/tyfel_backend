import json

from mongoengine import connect
from flask import Flask
from flask_cors import CORS

from consts import DB_HOST, DB_PORT
from mongo_adapter import select_documents
from documnets import Posts

app = Flask(__name__)
CORS(app)

connect('tyfel', host=DB_HOST, port=DB_PORT)


@app.route("/", methods=['GET'])
def root():
    return "Hi Eliya"


@app.route("/posts", methods=['GET'])
def get_posts():
    return json.dumps(select_documents(Posts))


app.run('0.0.0.0', 80, threaded=True)
