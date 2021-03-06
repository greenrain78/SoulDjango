from django.contrib import admin


# Register your models here.
from Rank.models import UserRank


@admin.register(UserRank)
class UserRankAdmin(admin.ModelAdmin):
    list_display = ('user', 'exp', 'tier')
