"""
get lots (hundreds-thousands) of games 

"""
import logging
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

    def getMatchList(self, player: str, num: int = 100) -> list[int]:
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
        match_history = cass.get_match_history(end_index=num, champions=summoner)
        print("His match history is length: {}".format(len(match_history)))
        return match_history

    def getMatchData(self, match_id):
        """

        :param matchId:
        :return:
        """
        return cass.get_match_history(match_id)

    def matchToJson(self, file_name, match):
        with open(file_name + ".json", "w+") as fh:
            fh.write(match.to_json())

    def writeMatches(self, match_list):
        """

        :param match_list:
        :return:
        """
        for mat


if __name__ == "__main__":
    """
    """
    crawlingContext = CrawlingContext("RGAPI-2f774048-8d86-4c98-a317-5230f8b1b898")

    faker_match_list = crawlingContext.getMatchList("Faker")



# faker_last_match_id = 2842707542
faker_last_match = cass.get_match(faker_last_match_id)

last_match_timeline = faker_last_match.timeline
print("last match frames: {}".format(len(last_match_timeline.frames)))
print("match length: {}".format(faker_last_match.duration))

last_match_frames = last_match_timeline.frames



# # write to CSV

with open(data_folder_name + "/" + file_name + ".csv", 'w+') as csvfile:
    frame_writer = csv.writer(csvfile)
    header = "matchId, timestamp, positionX, positionY, creepScore, currentGold, dominionScore, experience, goldEarned, level, neutralMinionsKilled, participantId, teamScore"
    header = [word for word in header.replace(',', '').split(' ')]
    frame_writer.writerow(header)

    # write data out to files 
    for frame in last_match_frames:
        timestamp = frame.timestamp
        print("Timestamp {}".format(timestamp))

        participantFrames = [value.to_dict() for key, value in frame.participant_frames.items()]
        for pframe in participantFrames:
            try:
                pos_x = pframe['position']['x']
                pos_y = pframe['position']['y']
            except:
                pos_x = 0
                pos_y = 0
            row = [faker_last_match_id, timestamp, pos_x, pos_y]
            columns = [
                'creepScore',
                'currentGold',
                'dominionScore',
                'experience',
                'goldEarned',
                'level',
                'neutralMinionsKilled',
                'participantId',
                'teamScore'
            ]
            for col in columns:
                try:
                    row.append(pframe[col])
                except:
                    continue

            print(row)
            frame_writer.writerow(row)
