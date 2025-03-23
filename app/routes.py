from flask import Blueprint, jsonify
from flask_jwt_extended import get_jwt, jwt_required

from app.limiter import dynamic_rate_limit, limiter
from app.tasks import enqueue_task

api_bp = Blueprint('api', __name__)

@api_bp.route('/ai-task', methods=['POST'])
@jwt_required()
@limiter.limit(dynamic_rate_limit)
def ai_task():
    claims = get_jwt()
    task_id = enqueue_task(claims.get('tier', 'free'))
    return jsonify({'task_id': task_id, 'status': 'queued'})
