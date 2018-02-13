from django.db import models
from django.utils import timezone
import datetime


class Post(models.Model):
    post_title = models.CharField(max_length=30)
    post_text = models.CharField(max_length=12)
    publication_date = models.DateTimeField('date of publication')

    def __str__(self):
        return self.post_title

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.publication_date <= now
    was_published_recently.admin_order_field = 'publication_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
