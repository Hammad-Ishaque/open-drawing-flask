from flask import Blueprint
from flask_socketio import emit
from app import socketio
from app import redis_client

websocket_bp = Blueprint('websocket', __name__)

@socketio.on('request_status')
def send_status(task_id):
    status = redis_client.get(task_id) or "queued"
    emit('status_update', {'task_id': task_id, 'status': status})
