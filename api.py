import json

from mongoengine import connect
from flask import Flask
from flask_cors import CORS

from consts import DB_HOST, DB_PORT
from mongo_adapter import select_documents
from documnets import Posts
from small_talk import start_conversation

app = Flask(__name__)
CORS(app)

connect('tyfel', host=DB_HOST, port=DB_PORT)


@app.route("/", methods=['GET'])
def root():
    return "Hi Eliya"


@app.route("/posts", methods=['GET'])
def get_posts():
    return json.dumps(select_documents(Posts))


@app.route("/small_talk", methods=['GET'])
def start_meeting():
    return start_conversation()


app.run('localhost', 80, threaded=True)
