from django.db import models

# Create your models here.
from django.utils import timezone


class User(models.Model):
    # name
    name = models.CharField(max_length=10)
    nickname = models.CharField(max_length=30)
    baekjoon_id = models.CharField(max_length=100, null=True, unique=True)

    # number
    number = models.PositiveBigIntegerField(default=0)
    email = models.CharField(max_length=200)

    # time
    joined_time = models.DateTimeField(default=timezone.now)
    birthday = models.DateTimeField(default=timezone.now,  null=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.nickname

    def publish(self):
        self.published_date = timezone.now()
        self.save()


