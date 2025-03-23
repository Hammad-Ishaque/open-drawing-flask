from flask_jwt_extended import get_jwt, verify_jwt_in_request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from app import app

limiter = Limiter(get_remote_address, app=app, storage_uri='redis://redis:6379')


# Function to determine rate limit dynamically
def dynamic_rate_limit():

    try:
        verify_jwt_in_request()
        claims = get_jwt()

        tier = claims.get("tier", "free")

        return {
            'free': '1 per minute',
            'pro': '10 per minute',
            'enterprise': '1000 per minute'
        }.get(tier, '1 per minute')

    except Exception:
        return '1 per minute'
