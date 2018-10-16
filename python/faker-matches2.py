"""
get lots (hundreds-thousands) of games
data we want:


"""

import json
from src.riot import Riot
import csv

stats_list = [
    'participantId',
    'win',
    'item0',
    'item1',
    'item2',
    'item3',
    'item4',
    'item5',
    'item6',
    'kills',
    'deaths',
    'assists',
    'largestKillingSpree',
    'largestMultiKill',
    'killingSprees',
    'longestTimeSpentLiving',
    'doubleKills',
    'tripleKills',
    'quadraKills',
    'pentaKills',
    'unrealKills',
    'totalDamageDealt',
    'magicDamageDealt',
    'physicalDamageDealt',
    'trueDamageDealt',
    'largestCriticalStrike',
    'totalDamageDealtToChampions',
    'magicDamageDealtToChampions',
    'physicalDamageDealtToChampions',
    'trueDamageDealtToChampions',
    'totalHeal',
    'totalUnitsHealed',
    'damageSelfMitigated',
    'damageDealtToObjectives',
    'damageDealtToTurrets',
    'visionScore',
    'timeCCingOthers',
    'totalDamageTaken',
    'magicalDamageTaken',
    'physicalDamageTaken',
    'trueDamageTaken',
    'goldEarned',
    'goldSpent'
]


class Match:
    def __init__(self, match_json):
        self.json = match_json

    def getParticipantId(self, name):
        part_ident = self.json["participantIdentities"]
        player = [p for p in part_ident if p["player"]["summonerName"] == name][0]["participantId"]
        return player


def tryone():
    riot_api_key = "RGAPI-2f774048-8d86-4c98-a317-5230f8b1b898"
    api = Riot(riot_api_key)

    faker = api.getSummonerByName("Faker")
    account_id = faker["accountId"]
    match_list = api.getMatchList(account_id)["matches"]

    with open("data/faker-match-list.json", "w+") as fh:
        fh.write(json.dumps(match_list, indent=4))

    for match in match_list:
        match_id = match["gameId"]
        match_json = api.getMatch(match_id)
        file_name = "data/" + "match-" + str(match_id) + ".json"
        fh = open(file_name, "w+")
        fh.write(json.dumps(match_json, indent=2))
        fh.close()


if __name__ == "__main__":
    """
    """
    riot_api_key = "RGAPI-9d4bf446-9a91-46d6-aa18-1e7aae10e366"
    api = Riot(riot_api_key)

    faker = api.getSummonerByName("Faker")
    account_id = faker["accountId"]
    match_list = api.getMatchList(account_id)["matches"]

    fh = open("data/matchstats.csv", "w+")
    csv_writer = csv.writer(fh)
    csv_writer.writerow(["matchid"] + stats_list)

    for match in match_list:
        match_id = match["gameId"]
        match_json = api.getMatch(match_id)

        try:
            match_json["participants"]
        except: 
            continue

        for participant in match_json["participants"]:
            stats = participant["stats"]
            row = [match_id]
            for stat in stats_list:
                row.append(stats[stat])
            csv_writer.writerow(row)

    fh.close()
