from celery import Celery


def make_celery(app_name='worker'):
    return Celery(app_name, backend='redis://redis:6379/0', broker='redis://redis:6379/0')

celery = make_celery()
