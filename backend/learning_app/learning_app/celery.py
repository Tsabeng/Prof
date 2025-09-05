from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning_app.settings')
app = Celery('learning_app')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()