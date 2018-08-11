from django.db import models
from django.utils import timezone


class Comment(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    message = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Login(models.Model):
    name = models.CharField(max_length=70, blank=True)
    email = models.EmailField(max_length=70, blank=True)
    password = models.CharField(max_length=10, blank=True)
    repeat_password = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.name
