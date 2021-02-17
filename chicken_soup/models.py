from django.db import models


# Create your models here.
from django.utils import timezone


class User(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    nickname = models.CharField(max_length=30)
    number = models.PositiveBigIntegerField(default=0)
    email = models.CharField(max_length=200)
    joined_time = models.DateTimeField(default=timezone.now)
    birthday = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nickname
