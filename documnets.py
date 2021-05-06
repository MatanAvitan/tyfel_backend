from datetime import datetime
from mongoengine import *


class Posts(Document):
    username = StringField(required=True)
    creation_date = DateField(required=True, default=datetime.now)
    title = StringField(required=True)
    body = StringField(required=True)
    comments = ListField(required=True)
