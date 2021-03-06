from django.forms import ModelForm

from Rank.models import UserRank


class UserRankForm(ModelForm):
    class Meta:
        model = UserRank
        fields = ['user', 'exp', 'tier', 'higher_rating', 'class_rating', 'solved_rating', 'vote_count_rating']
