from django.db import models
from django.utils import timezone

class News(models.Model):
    THEMES = (
        ('theme1', 'Политика'),
        ("theme2", "Регионы"),
        ("theme3", "Инвестиции")
    )

    date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=200)
    article_text = models.TextField()
    theme = models.CharField(max_length=50, choices=THEMES, default='')

    def __str__(self):
        return self.title
