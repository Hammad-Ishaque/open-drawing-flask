import time

from redis import Redis

from worker.celery_config import celery

redis_client = Redis(host='redis', port=6379, decode_responses=True)

@celery.task
def process_ai_task(task_id):
    redis_client.set(task_id, 'processing')
    time.sleep(5)  # Simulate AI processing
    redis_client.set(task_id, 'completed')
    return "Task completed!"
