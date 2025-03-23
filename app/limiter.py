from app import app
from flask_jwt_extended import get_jwt
from flask_jwt_extended import verify_jwt_in_request

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


limiter = Limiter(get_remote_address, app=app, storage_uri='redis://redis:6379')


# Function to determine rate limit dynamically
def dynamic_rate_limit():

    try:
        verify_jwt_in_request()  # Ensure JWT exists
        claims = get_jwt()  # ✅ Retrieve claims instead of identity

        tier = claims.get("tier", "free")  # ✅ Extract tier safely

        return {
            "free": "1 per minute",
            "pro": "10 per minute",
            "enterprise": "1000 per minute"
        }.get(tier, "1 per minute")

    except Exception as e:
        print(f"Rate limit error: {e}")  # Debug logs
        return "1 per minute"  # Default to safe limit
