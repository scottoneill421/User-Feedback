from django.db import models

class SubmittedForm(models.Model):
    subject = models.CharField(max_length=50)
    author = models.CharField(max_length=250)
    body = models.TextField()
    screenshot = models.ImageField(default="default.png", blank=True)
    time_published = models.DateTimeField(auto_now=True)
