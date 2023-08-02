import os
from celery import Celery

from podle.settings import RABBIT_BROKER_URL

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "podle.settings")
app = Celery(
    "podle",
    broker=RABBIT_BROKER_URL,
    broker_connection_retry_on_startup=True,
)
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(["apis"])


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

