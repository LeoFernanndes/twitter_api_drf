from celery import Celery


CELERY_BEAT_SCHEDULE = {
    "run-me-every-ten-seconds": {
        "task": "twitter.celery.check",
        "schedule": 60.0
    }
}

app = Celery(
    'celery',broker="redis://localhost:6379/0",
    include=['users.tasks']
)

@app.task
def check():
 print("I am checking your stuff")
 return('check')


app.conf.beat_schedule = CELERY_BEAT_SCHEDULE #TODO move this dictionary to settings