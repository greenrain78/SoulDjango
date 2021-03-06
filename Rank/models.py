from django.db import models

# Create your models here.
from django.utils import timezone

from chicken_soup.models import User


class UserRank(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)

    # level
    exp = models.IntegerField(default=0)
    tier = models.CharField(max_length=50, default="unranked")

    # rating
    higher_rating = models.IntegerField(default=0)
    class_rating = models.IntegerField(default=0)
    solved_rating = models.IntegerField(default=0)
    vote_count_rating = models.IntegerField(default=0)




    # 날짜
    modify_date = models.DateTimeField(auto_now=True)

