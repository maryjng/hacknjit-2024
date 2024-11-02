from flask import Flask, g
from flask_wtf import CSRFProtect
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import certifi

from .config import Config

client = MongoClient(Config.CONNECTION_STRING, tlsCAFile=certifi.where())
db = client['hackathon2024-dev']

csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    csrf.init_app(app)
    
    from .auth.routes import auth_bp
    from .main.routes import main_bp
    
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(main_bp, url_prefix='/')
    
    @app.before_request
    def before_request():
        g.db = db
    
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    return app


