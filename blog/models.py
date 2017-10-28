from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    pubhished_date = models.DateTimeField(
              blank =True, null=True)
# Create your models here.
    def publish(self):
        self.pubhished_date = timezone.now()
        self.save()

    def _srt_(self):
        return self.title
