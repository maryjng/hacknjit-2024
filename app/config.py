import os
from dotenv import load_dotenv


def load_environment():
    load_dotenv()
    env_mode = os.getenv('ENV_MODE')

    if env_mode == 'production':
        load_dotenv('.env.production')
    else:
        load_dotenv('.env.development')

load_environment()

class Config:
    SECRET_KEY=os.getenv('SECRET_KEY')
    CONNECTION_STRING=os.getenv('CONNECTION_STRING')

    # client = MongoClient(CONNECTION_STRING, tlsCAFile=certifi.where())

