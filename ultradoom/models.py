from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=55)
    embed = models.TextField(null=True, blank=True)