import sys
from flask import Flask
from database.db import initialize_db
from flask_restful import Api
from resources.routes import initialize_routes
from flask_bcrypt import Bcrypt

# Define a flask app
app = Flask(__name__)
api = Api(app)
#default config
host = 'localhost'
port = 5000
debug = False

# CLI arguments of custom config
try:
    host = sys.argv[1]
    port = sys.argv[2]
    debug = sys.argv[3]
except:
    pass

DB_URI = "mongodb+srv://soham:sohamSIH@cluster0.ywiiw.gcp.mongodb.net/care?retryWrites=true&w=majority"

app.config["MONGODB_HOST"] = DB_URI

initialize_db(app)
initialize_routes(api)
bcrypt = Bcrypt(app)

if __name__ == "__main__":
    app.run(host, port, debug)