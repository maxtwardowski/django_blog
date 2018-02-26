from django.db import models
from django.utils import timezone
import datetime


class Post(models.Model):
    title = models.CharField(max_length=30)
    text = models.CharField(max_length=100000)
    date = models.DateTimeField('date of publication')
    image = models.FileField(null=True, blank=True, upload_to='uploads/images')

    def __str__(self):
        return self.title

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.date <= now
    was_published_recently.admin_order_field = 'date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Comment(models.Model):
    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.CharField(max_length=30)
    text = models.CharField(max_length=10000)
    date = models.DateTimeField('date of publication')
    approved = models.BooleanField(default=True)  # SHOULD BE FALSE IN FINAL!!!

    def __str__(self):
        return self.author

    def approvecomment(self):
        self.approved = True
        self.save()
