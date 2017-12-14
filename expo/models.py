from django.db import models
from django.utils import timezone

class Painting(models.Model):
    artist = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateField(blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title