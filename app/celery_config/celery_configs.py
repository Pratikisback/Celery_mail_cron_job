import os
from celery import Celery
from celery.schedules import crontab


def make_celery(flask_app):
    try:
        # Initialize Celery
        celery_app = Celery(
            flask_app,
            # broker=flask_app.config['broker_url'],
            broker=['amqp://localhost:5672//'],
            include=['app.celery_config.celery_tasks']
        )
        flask_app.config['beat_schedule'] = {
            # Executes every minute
            'periodic_task-every-minute': {
                'task': 'send_emails',
                'schedule': crontab(hour="12", minute="0")
            }
        }

        celery_app.conf.update(flask_app.config)
        TaskBase =  celery_app.Task

        class ContextTask(TaskBase):
            abstract = True

            def __call__(self, *args, **kwargs):
                with flask_app.app_context():
                    return TaskBase.__call__(self, *args, **kwargs)

        celery_app.Task = ContextTask
        return celery_app

    except Exception as e:
        return str(e)
