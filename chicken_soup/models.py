from django.db import models

# Create your models here.
from django.utils import timezone


class User(models.Model):
    # name
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    nickname = models.CharField(max_length=30)

    # number
    number = models.PositiveBigIntegerField(default=0)
    email = models.CharField(max_length=200)
    correct = models.IntegerField(default=0)
    submission = models.IntegerField(default=0)
    answer_ratio = models.FloatField(default=0.5)

    # time
    joined_time = models.DateTimeField(default=timezone.now)
    birthday = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.nickname

    def publish(self):
        self.published_date = timezone.now()
        self.save()
