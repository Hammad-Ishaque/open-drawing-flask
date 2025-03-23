from flask import Blueprint
from flask import jsonify
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt
from app.limiter import dynamic_rate_limit
from app.limiter import limiter

from app.tasks import enqueue_task

api_bp = Blueprint('api', __name__)

@api_bp.route('/ai-task', methods=['POST'])
@jwt_required()
@limiter.limit(dynamic_rate_limit)
def ai_task():
    print('this is hammad')
    claims = get_jwt()
    task_id = enqueue_task(claims.get("tier", "free"))
    return jsonify({"task_id": task_id, "status": "queued"})
