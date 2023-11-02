from flask import Flask
from flask_restful import Api
from pymongo import MongoClient
from app.celery_config.celery_configs import make_celery

flask_app = Flask(__name__)
api = Api(flask_app)
client = MongoClient("mongodb://localhost:27017")
db = client['my_test']
collection = db['my_collection']


# flask_app.config['broker_url'] = 'amqp://rabbitmq:5672//'
# flask_app.config['backend'] = 'redis://localhost:6379/0'
flask_app.config['event_serializer'] = 'json'
flask_app.config['result_serializer'] = 'json'
flask_app.config['task_serializer'] = 'json'
celery_app = make_celery(flask_app)