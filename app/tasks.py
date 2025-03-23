import uuid

from redis import Redis

from worker.worker import process_ai_task

# Redis connection
redis_client = Redis(host='redis', port=6379, decode_responses=True)

def enqueue_task(user_tier):
    """Add a new AI task to the queue based on user priority."""
    task_id = str(uuid.uuid4())  # Generate unique task ID

    # Set initial status in Redis
    redis_client.set(task_id, "queued")

    # Prioritize Pro & Enterprise users
    priority = {"free": 3, "pro": 2, "enterprise": 1}
    countdown = priority.get(user_tier, 3) * 2  # Delay based on user tier

    # Enqueue task with priority
    process_ai_task.apply_async(args=[task_id], countdown=countdown)

    return task_id
