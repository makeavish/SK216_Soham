from .db import db
import datetime
from flask_bcrypt import generate_password_hash, check_password_hash

class Results(db.Document):
    title = db.StringField(required=True)
    url = db.StringField(required=True)
    text = db.StringField(required=True)
    imageUrl = db.StringField(required=True)
    score = db.StringField(required=True)

class Crawl(db.Document):
    query = db.StringField(required=True)
    results = db.ListField(db.ReferenceField(Results))
    runDate = db.DateTimeField(default=datetime.datetime.utcnow)

class User(db.Document):
    name = db.StringField()
    email = db.StringField(required=True, unique=True)
    password = db.StringField()
    registerDate = db.DateTimeField(default=datetime.datetime.utcnow)
    crawls = db.ListField(db.ReferenceField(Crawl))
    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')
    def check_password(self, password):
        return check_password_hash(self.password, password)
