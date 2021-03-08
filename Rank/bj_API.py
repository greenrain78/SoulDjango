import asyncio
import json
import math

import requests


class SolvedAcAPI:
    BASE_URL = 'https://api.solved.ac'
    version = 'v2'

    @property
    def api_url(self) -> str:
        return f'{self.BASE_URL}/{self.version}'

    def fetch_user_info(self, name: str):
        url = f'{self.api_url}/users/show.json?id={name}'
        response = requests.get(url)
        json_resp = response.json()
        if response.status_code != 200:
            raise ValueError(json_resp.get('message', 'API Error'))
        # get user info
        print(json_resp)
        if json_resp.get('success'):
            userInfo = json_resp.get('result').get('user')
            return userInfo[0]
        else:
            return None

    def fetch_user_problem(self, name: str):
        url = f'{self.api_url}/users/problem_stats.json?id={name}'
        response = requests.get(url)
        json_resp = response.json()
        if response.status_code != 200:
            raise ValueError(json_resp.get('message', 'API Error'))
        # get user problem
        userProblem = json_resp.get('result')
        return userProblem


#
# tmp = SolvedAcAPI()
# print(asyncio.run(tmp.fetch_user_info('kdw010130')))

class Rating:
    @staticmethod
    def levelName(level):
        if level == 0:
            return 'Unrated'
        if level == 31:
            return 'Master'
        prefix = ['Bronze', 'Silver', 'Gold', 'Platinum', 'Diamond', 'Ruby']
        roman = ['I', 'II', 'III', 'IV', 'V']
        return prefix[math.floor((level - 1) / 5)] + ' ' + roman[4 - (level - 1) % 5]

    @classmethod
    def user_Rating(cls, user_info, problem_stat):
        result = {}
        result['exp'] = user_info['exp']
        result['tier'] = cls.levelName(user_info['level'])

        cnt = 0
        higher_rating = 0
        for i in range(30, 0, -1):
            now_cnt = min(100 - cnt, problem_stat[i]['solved'])
            cnt += now_cnt
            higher_rating += (now_cnt * i)

        result['higher_rating'] = higher_rating

        # 보너스 레이팅 계산
        class_info = user_info['class']
        solved_info = user_info['solved']
        vote_count_info = user_info['vote_count']

        class_rating_table = [0, 25, 50, 100, 150, 200, 210, 220, 230, 240, 250]
        class_rating = class_rating_table[class_info]
        solved_rating = round(175 * (1 - pow(0.995, solved_info)))
        vote_count_rating = round(25 * (1 - pow(0.9, vote_count_info)))

        result['class_rating'] = class_rating
        result['solved_rating'] = solved_rating
        result['vote_count_rating'] = vote_count_rating

        # 새로운 티어 계산
        # new_rating = higher_rating + class_rating + solved_rating + vote_count_rating
        # new_tier = 31
        # new_tier_table = [0, 30, 60, 90, 120, 150,
        #                   200, 300, 400, 500, 650,
        #                   800, 950, 1100, 1250, 1400,
        #                   1600, 1750, 1900, 2000, 2100,
        #                   2200, 2300, 2400, 2500, 2600,
        #                   2700, 2800, 2850, 2900, 2950, 3000]
        # for i in range(31):
        #     if new_tier_table[i] <= new_rating < new_tier_table[i + 1]:
        #         new_tier = i
        #         break
        #
        # print('새로운 레이팅 :', new_rating)
        # print('새로운 티어 :', levelName(new_tier))
        return result
