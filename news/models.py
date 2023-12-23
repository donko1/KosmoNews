from django.db import models
from django.utils import timezone
from django.conf import settings

class News(models.Model):
    image = models.ImageField(upload_to='images/', default="none")
    THEMES = settings.THEMES
    date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=200)
    article_text = models.TextField()
    theme = models.CharField(max_length=50, choices=THEMES, default='')

    def __str__(self):
        return self.title
