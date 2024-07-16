import os
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import News
from datetime import datetime

@receiver(post_save, sender=News)
def log_news_creation(sender, instance, created, **kwargs):
    if created:
        log_message = f"News Created: {instance.title}, Created at: {datetime.now()}\n"
        log_file_path = os.path.join(os.path.dirname(__file__), 'news_log.txt')

        with open(log_file_path, 'a') as log_file:
            log_file.write(log_message)

@receiver(post_delete, sender=News)
def log_news_deletion(sender, instance, **kwargs):
    log_message = f"News Deleted: {instance.title}, Deleted at: {datetime.now()}\n"
    log_file_path = os.path.join(os.path.dirname(__file__), 'news_log.txt')

    with open(log_file_path, 'a') as log_file:
        log_file.write(log_message)