# go to 
# and reset API key
# then CTRL+C CTRL+V it below 

import cassiopeia as cass
from os.path import dirname, abspath


riot_api_key = "RGAPI-77619554-7949-4393-be68-5e643092e8b4"

config = cass.get_default_config()

# stores data to disk 
# doesn't work with match history :( 
config["pipeline"]["SimpleKVDiskStore"] =  {
        "package": "cassiopeia_diskstore",
        "path": "{}/data".format(dirname(abspath(__file__)))
    }
    
# # SQLStore not yet working 
# config["pipeline"]["SQLStore"] =  {
#         "package": "cassiopeia_sqlstore",
#         "path": "sqlite:///{}/data/foo.db".format(dirname(abspath(__file__)))
#     }

cass.apply_settings(config)
cass.set_riot_api_key(riot_api_key)  
cass.set_default_region("NA")

# Faker is the top rated player in LOL 
summoner = cass.get_summoner(name="Faker")
print("{accountId}: {name} is a level {level} summoner on the {region} server."\
      .format(accountId=summoner.id, 
              name=summoner.name, 
              level=summoner.level, 
              region=summoner.region)
     )

# 
# get Faker's match history his last match

# faker_match_history = summoner.match_history
# print("His match history is length: {}".format(len(faker_match_history)))

# faker_last_match_id = faker_match_history[0].id
faker_last_match_id = 2842707542
faker_last_match = cass.get_match(faker_last_match_id)


last_match_timeline = faker_last_match.timeline
print("last match frames: {}".format(len(last_match_timeline.frames)))
print("match length: {}".format(faker_last_match.duration))

last_match_frames = last_match_timeline.frames

# make a data folder 
from os import direxists, path, getcwd, mkdir
data_folder_name = "data"
pwd = getcwd()
full_path = path.join(pwd, data_folder_name)
if not direxists(full_path):
    mkdir(full_path)

# write data out to files 
for frame in last_match_frames:
    timestamp = frame.timestamp
    print("Timestamp {}".format(timestamp))
    json_frame = frame.to_json()
    print(json_frame)
    file_name = "{}-{}.json".format(faker_last_match_id, timestamp)
    with open(file_name, 'w') as fh:
        fh.write(json_frame)
