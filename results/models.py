from django.db import models

# Create your models here.
class Events(models.Model):
    title = models.TextField(null=True, blank=False)
    message = models.TextField(null=True, blank=False)
    time_begin = models.DateTimeField(auto_now_add=False, blank=True)
    time_end = models.DateTimeField(auto_now_add=False, blank=True)
