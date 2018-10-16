"""
get lots (hundreds-thousands) of games
data we want:


"""
import logging
import json
import cassiopeia as cass
from src.tools import make_data_folder
import csv


class CrawlingContext:
    def __init__(self, riot_api_key, default_region="NA"):
        """

        :param riot_api_key: the key you will be using today
        """
        self.riot_api_key = riot_api_key

        cass.set_riot_api_key(riot_api_key)
        cass.set_default_region(default_region)

    def getMatchList(self, player, num=100):
        """
        get num matches for player
        :param player: summoner name
        :param num: number of matches
        :return: List[int]
        """
        summoner = cass.get_summoner(name=player)
        print("{accountId}: {name} is a level {level} summoner on the {region} server."
              .format(accountId=summoner.id,
                      name=summoner.name,
                      level=summoner.level,
                      region=summoner.region)
              )
        match_history = cass.get_match_history(summoner, end_index=num)
        print("His match history is length: {}".format(len(match_history)))
        return match_history

    def getMatch(self, match_id):
        return cass.get_match(match_id)

    def matchToJson(self, file_name, match):
        with open(file_name + ".json", "w+") as fh:
            fh.write(match.to_json())


stats = [
    "altars_captured",
    "altars_neutralized",
    "assists",
    "combat_player_score",
    "damage_dealt_to_objectives",
    "damage_dealt_to_turrets",
    "damage_self_mitigated",
    "deaths",
    "double_kills",
    "first_blood_assist",
    "first_blood_kill",
    "first_inhibitor_assist",
    "first_inhibitor_kill",
    "first_tower_assist",
    "first_tower_kill",
    "gold_earned",
    "gold_spent",
    "inhibitor_kills",
    "items",
    "kda",
    "killing_sprees",
    "kills",
    "largest_critical_strike",
    "largest_killing_spree",
    "largest_multi_kill",
    "level",
    "longest_time_spent_living",
    "magic_damage_dealt",
    "magic_damage_dealt_to_champions",
    "magical_damage_taken",
    "neutral_minions_killed",
    "neutral_minions_killed_enemy_jungle",
    "neutral_minions_killed_team_jungle",
    "node_capture",
    "node_capture_assist",
    "node_neutralize",
    "node_neutralize_assist",
    "objective_player_score",
    "penta_kills",
    "physical_damage_dealt",
    "physical_damage_dealt_to_champions",
    "physical_damage_taken",
    "quadra_kills",
    "sight_wards_bought_in_game",
    "team_objective",
    "time_CCing_others",
    "total_damage_dealt",
    "total_damage_dealt_to_champions",
    "total_damage_taken",
    "total_heal",
    "total_minions_killed",
    "total_player_score",
    "total_score_rank",
    "total_time_crowd_control_dealt",
    "total_units_healed",
    "triple_kills",
    "true_damage_dealt",
    "true_damage_dealt_to_champions",
    "true_damage_taken",
    "turret_kills",
    "unreal_kills",
    "vision_score",
    "vision_wards_bought_in_game",
    "wards_killed",
    "wards_placed",
    "win"
]

if __name__ == "__main__":
    """
    """
    riot_api_key = "RGAPI-2f774048-8d86-4c98-a317-5230f8b1b898"
    make_data_folder()
    cass.set_riot_api_key(riot_api_key)
    cass.set_default_region("NA")

    summoner = cass.get_summoner(name="Faker")

    match_history = summoner.match_history

    csv_handle = open("data/faker-stats.csv", "w+")
    csv_writer = csv.writer(csv_handle)
    csv_writer.writerow(["match_id", "rowlen"] + stats)

    for match in match_history:
        match = cass.get_match(match.id)
        match_json = json.loads(match.to_json())
        participants_list = match_json["participants"]
        if len(participants_list) < 2:
            continue
        faker_stats = [player for player in participants_list if player["summonerName"] == "Faker"][0]
        row = []
        for stat in stats:
            row.append(faker_stats[stat])

        row = [str(match.id), str(len(row))] + row
        csv_writer.writerow(row)

    csv_handle.close()
