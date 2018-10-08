import json
import requests
import typing


class Riot:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_arg = "?api_key=" + api_key
        self.url_base = "https://na1.api.riotgames.com"
        self.routes = {
            "matches": "/lol/match/v3/matches",
            "summoners/by-name": "/lol/summoner/v3/summoners/by-name",
            "matchlist": "/lol/match/v3/matchlists/by-account"
        }

    def getUrl(self, endpoint, arg):
        return self.url_base + self.routes[endpoint] + "/" + str(arg) + self.api_arg

    def getMatchList(self, account_id):
        url = self.getUrl("matchlist", account_id)
        return requests.get(url).json()

    def getSummonerByName(self, name):
        url = self.getUrl("summoners/by-name", name)
        return requests.get(url).json()

    def getMatch(self, id):
        url = self.getUrl("matches", id)
        response = requests.get(url)
        return response.json()


if __name__ == "__main__":
    key = "RGAPI-2f774048-8d86-4c98-a317-5230f8b1b898"
    api = Riot(key)
    match = api.getMatch("2842707542")
    print(match)
