import json
import requests
from requests import Response


class RateLimitException(Exception):
    """basic exception """
    pass


class Riot:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_arg = "?api_key=" + api_key
        self.url_base = "https://na1.api.riotgames.com"
        self.routes = {
            "matches": "/lol/match/v3/matches",
            "summoners/by-name": "/lol/summoner/v3/summoners/by-name",
            "matchlist": "/lol/match/v3/matchlists/by-account",
            "featuredMatches": "/lol/spectator/v3/featured-games"
        }

    def checkStatus(self, response: Response):
        status_code = response.status_code
        if status_code == 429:
            raise RateLimitException()

    def getUrl(self, endpoint, arg):
        return self.url_base + self.routes[endpoint] + "/" + str(arg) + self.api_arg

    def getMatchList(self, account_id):
        url = self.getUrl("matchlist", account_id)
        response = requests.get(url)
        self.checkStatus(response)
        return response.json()

    def getSummonerByName(self, name):
        url = self.getUrl("summoners/by-name", name)
        response = requests.get(url)
        self.checkStatus(response)
        return response.json()

    def getMatch(self, id):
        url = self.getUrl("matches", id)
        response: Response = requests.get(url)
        self.checkStatus(response)
        return response.json()

    def getFeaturedMatches(self):
        url = self.url_base + self.routes["featuredMatches"] + self.api_arg
        response = requests.get(url)
        self.checkStatus(response)
        return response.json()


if __name__ == "__main__":
    key = "RGAPI-eb49c30b-3d29-4160-a19a-3ab744f48aa0"
    api = Riot(key)

    players = [
        'Faker',
        'Westdoor',
        'Marin',
        'ssumday',
        'huni',
        'bjergsen',
        'ziv',
        'aphromoo',
        'piccaboo',
        'bang',
        'doublelift',
        'pawn',
        'clearlove',
        'yellowstar',
        'deft',
        'pyl',
        'rookie',
        'kakao',
        'imp'
    ]
    for i in range(100):
        print(api.getFeaturedMatches())

