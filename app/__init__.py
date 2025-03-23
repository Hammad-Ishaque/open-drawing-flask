from flask import Flask
from flask_jwt_extended import JWTManager
from flask_socketio import SocketIO
from redis import Redis
import os

# Initialize Flask app
app = Flask(__name__)
app.config.from_object('app.config.Config')

# JWT
jwt = JWTManager(app)

# Rate Limiter (Redis backend)
redis_client = Redis(host=os.getenv('REDIS_HOST', 'redis'), port=6379, decode_responses=True)

# WebSockets
socketio = SocketIO(app, cors_allowed_origins="*")

from app.auth import auth_bp
from app.routes import api_bp
from app.websocket import websocket_bp
# Register Blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(api_bp, url_prefix='/api')
app.register_blueprint(websocket_bp, url_prefix='/ws')
