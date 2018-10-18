import json
import requests

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

    def getFeaturedMatches(self):
        url = self.url_base + self.routes["featuredMatches"] + self.api_arg
        response = requests.get(url)
        return response.json()


if __name__ == "__main__":
    key = "RGAPI-ac8d4e31-c857-4429-8615-db61b14cbb66"
    api = Riot(key)

    seed_act_id =

    featured_matches = api.getMatchList(seed_act_id)
    for match in featured_matches["gameList"]:
        match_id = match['gameId']
        match = api.getMatch(match_id)
        fh = open(str(match_id) + ".json", 'w+')
        fh.write(json.dumps(match, indent=2))
        fh.close()
