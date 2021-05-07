from datetime import datetime
from mongoengine import *


class Posts(Document):
    username = StringField(required=True)
    creation_date = DateField(required=True, default=datetime.now().isoformat)
    title = StringField(required=True)
    body = StringField(required=True)
    comments = ListField(required=True)
    image_path = StringField(required=True)
