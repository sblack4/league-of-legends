#!/bin/env
"""
the hierarchy of a match is like this:
match:

"""

# import logging
import traceback
# from sys import exc_info
import cassiopeia as cass
import pandas as pd


# file_name = __file__ + ".log"

# logging.basicConfig(file_name=file_name, level=logging.CRITICAL)


def get_or_else(dic, val, else_val):
    ret = else_val
    try:
        ret = dic.get(val, else_val)
    except Exception as e:
        logging.error(e)
    return ret


def getPosition(dic):
    retx= "0"
    rety= "0"
    try:
        retx = dic['position']['x']
        rety = dic['position']['y']
    except Exception as e:
        pass
        # logging.warning("given dict" + str(dic))
        # logging.error(e)
    return retx, rety


def get_participant_wins(match):
    """ given list of participants returns a dict of participantId -> win
    https://cassiopeia.readthedocs.io/en/latest/cassiopeia/match.html#cassiopeia.core.match.Participant
    :param participant_list:
    :return:
    """
    participant_list = match.participants
    participant_list.sort(key=id)
    ret = dict()
    for i in range(0, len(participant_list)):
        try:
            p = [x for x in participant_list if x.id == i + 1][0]
            ret[i + 1] = int(p.stats.win)
        except Exception as e:
            # pass
            # logging.error(e)
            ret[i + 1] = int(False)

    return ret


def get_match_history(summoner_name, n, offset=0):
    """

    :param summoner_name:
    :param n:
    :param offset:
    :return: generator that returns n-offset matches
    """
    summoner = cass.get_summoner(name=summoner_name)
    while n > offset:
        offset += 1
        yield cass.get_match_history(summoner=summoner,
                                     begin_index=offset-1,
                                     end_index=offset)


participant_frame_keys = [
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


frames_header = ["pos_x", "pos_y", "win"] + participant_frame_keys


def flatten_participant_frames(participant_frames, participant_wins):
    """ turns a participants frame object into a dataframe
    https://cassiopeia.readthedocs.io/en/latest/cassiopeia/match.html#cassiopeia.core.match.ParticipantFrame
    :param participant_frames:
    :param participant_wins:
    :return: dataframe with cols in frames_header
    """
    frames_df = pd.DataFrame(columns=frames_header)
    for i in range(1, len(participant_frames)):
        try:
            frame = participant_frames[i].to_dict()

            row = list()
            x, y = getPosition(frame)
            row.append(x)
            row.append(y)
            row.append(int(participant_wins[frame["participantId"]]))
            for k in participant_frame_keys:
                row.append(get_or_else(frame, k, "0"))

            new_dict = dict(zip(frames_header, row))
            new_df = pd.DataFrame(new_dict, index=[0])

            frames_df = frames_df.append(
                new_df,
                ignore_index=True)
        except Exception as e:
            pass
            # logging.error("Error with frame ")
            # logging.error(e)
            # logging.error(traceback.print_exc())

    return frames_df


event_keys = [
    'afterId',
    'ascendedType',
    'beforeId',
    'buildingType',
    'capturedPoint',
    'creatorId',
    'itemId',
    'killerId',
    'laneType',
    'levelUpType',
    'monsterSubType',
    'monsterType',
    'participantId',
    'skill',
    'teamId',
    'timestamp',
    'towerType',
    'type',
    'victimId',
    'wardType'
]

event_header = ['pos_x', 'pos_y', "win"] + event_keys


def flatten_events(events, participant_wins):
    """
    turn list of events into dataframe
    :param events:
    :return:
    """
    events_df = pd.DataFrame(columns=event_header)
    for evento in events:
        event = evento.to_dict()
        row = list()
        try:
            x, y = getPosition(event)
            row.append(x)
            row.append(y)

            participant_id = get_or_else(event, "participantId", "0")
            win = get_or_else(participant_wins, participant_id, "0")
            row.append(win)

            for k in event_keys:
                row.append(get_or_else(event, k, "0"))

            new_dict = dict(zip(event_header, row))
            new_df = pd.DataFrame(new_dict, index=[0])
            events_df = events_df.append(
                new_df,
                ignore_index=True)
        except Exception as e:
            pass
            # logging.error("Error with event parsing")
            # logging.error(e)
            # logging.error("".join(traceback.format_stack()))

    return events_df


def unpack_frame(frame, participant_wins):
    """ turns a frame object into two dataframes
    https://cassiopeia.readthedocs.io/en/latest/cassiopeia/match.html#cassiopeia.core.match.Frame
    :param frame:
    :param participant_wins: dictionary with participant_id: Int -> win: Bool
    :return: participants_frame, events_frame both as Dataframes
    """
    timestamp = frame.timestamp.total_seconds()
    events_df = flatten_events(frame.events, participant_wins)
    events_df['timestamp'] = timestamp
    participant_frames_df = flatten_participant_frames(frame.participant_frames, participant_wins)
    participant_frames_df['timestamp'] = timestamp
    return participant_frames_df, events_df


def unpack_timeline(timeline, participant_wins):
    """ turns a timeline object into two dataframes; one for participant_frames and one for events
    https://cassiopeia.readthedocs.io/en/latest/cassiopeia/match.html#cassiopeia.core.match.Timeline
    :param timeline:
    :return:
    """
    participant_frames_df = pd.DataFrame()
    events_df = pd.DataFrame()
    for frame in timeline.frames:
        pf_df, e_df = unpack_frame(frame, participant_wins)
        participant_frames_df = pd.concat([participant_frames_df, pf_df])
        events_df = pd.concat([events_df, e_df])
    return participant_frames_df, events_df


def write_matches(summoner_name, n):
    """
    writes n matches as csv files containing events or frames
    :param summoner_name: str of summoner name
    :param n: number of matches you want
    :return: void
    """
    participant_frames_df = pd.DataFrame()
    events_df = pd.DataFrame()

    summoner = cass.get_summoner(name="Faker")
    match_history = cass.get_match_history(summoner=summoner)

    i = 0
    for match in match_history:
        match_id = match.id
        match = cass.get_match(id=match_id)

        p_wins = get_participant_wins(match)

        pf_df, e_df = unpack_timeline(match.timeline, p_wins)
        pf_df['summoner'] = summoner_name
        e_df['summoner'] = summoner_name
        pf_df['match_id'] = match_id
        e_df['match_id'] = match_id

        participant_frames_df = pd.concat([participant_frames_df, pf_df])
        events_df = pd.concat([events_df, e_df])

        i += 1
        if i >= n:
            break

    participant_frames_df.to_csv(
        "participant_frames.csv",
        header=True,
        index=False
    )
    events_df.to_csv(
        "events.csv",
        header=True,
        index=False
    )


if __name__ == "__main__":
    """
    """
    riot_api_key = "RGAPI-8a53d848-db15-43b7-b135-5c8101ad4bba"

    cass.set_riot_api_key(riot_api_key)
    cass.set_default_region("NA")

    write_matches("Faker", 100)




