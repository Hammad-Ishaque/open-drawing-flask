import os
from datetime import timedelta


class Config:
    """Base configuration settings."""

    # Flask General Config
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")  # Change this in production
    DEBUG = True

    # JWT Configuration
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwtsecret")  # Change this in production
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=2)  # JWT token expiration time

    # Redis Configuration
    REDIS_HOST = os.getenv("REDIS_HOST", "redis")
    REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

    # Celery Configuration
    CELERY_BROKER_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/0"
    CELERY_RESULT_BACKEND = f"redis://{REDIS_HOST}:{REDIS_PORT}/0"

    # Rate Limiting (Handled in `limiter.py`)
    RATE_LIMITS = {
        "free": "1 per minute",
        "pro": "10 per minute",
        "enterprise": "1000 per minute"
    }
    PROPAGATE_EXCEPTIONS = True
