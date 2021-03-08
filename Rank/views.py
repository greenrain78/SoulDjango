from time import time

from django.shortcuts import render

# Create your views here.
from Rank.bj_API import SolvedAcAPI, Rating
from Rank.models import UserRank


def rank_list(request):
    # print(UserRank.objects.all())
    # for user_rank in UserRank.objects.all():
    # a.higher_rating = 10
    # print(a)
    # print(a.user)
    # a.save()
    begin = time()
    refresh()
    end = time()
    api_time = end - begin
    print('실행 시간: {0:.3f}초'.format(api_time))
    content = {'user_rank_list': UserRank.objects.all(), 'api_time': api_time}
    return render(request, 'ranking.html', content)


def detail(request):
    return None


def refresh():
    api_client = SolvedAcAPI()
    for user_rank in UserRank.objects.all():
        res_info = api_client.fetch_user_info(user_rank.user.baekjoon_id)
        if res_info:
            res_problem = api_client.fetch_user_problem(user_rank.user.baekjoon_id)
            rate = Rating.user_Rating(res_info, res_problem)
            user_rank.exp = rate['exp']
            user_rank.tier = rate['tier']
            user_rank.higher_rating = rate['higher_rating']
            user_rank.class_rating = rate['class_rating']
            user_rank.solved_rating = rate['solved_rating']
            user_rank.vote_count_rating = rate['vote_count_rating']
            user_rank.save()

