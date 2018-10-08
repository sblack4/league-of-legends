# league of legends 
Get API data, transform data, make predictions on data 


## Running 

1. Head to https://developer.riotgames.com/ and get yourself an account. 
2. login -> my dashboard -> `REGENERATE API KEY` -> copy key
3. paste key into file
4. run! 


## resources 
- [cassiopia](https://github.com/meraki-analytics/cassiopeia), a python library for the Riot API ([docs](https://cassiopeia.readthedocs.io/en/latest/#))
- [weka](https://www.cs.waikato.ac.nz/ml/weka/) for predictions 
- [frontail](https://github.com/mthenw/frontail) for monitoring remote job  
- RIP [lolking.net](http://www.lolking.net/)



## changelog 
given as monday of that week's changes


### 2018-10-01 `lol02.py`
script pulls down game into single csv file like below 
```
matchId,timestamp,positionX,positionY,creepScore,currentGold,dominionScore,experience,goldEarned,level,neutralMinionsKilled,participantId,teamScore
2842707542,0:00:00,1102,1180,0,1400,0,660,1400,1,0,1,0
```


### 2018-10-08 `lol03.py`
- [ ] get lots of game data (hundred or thousands)
- [ ] see if gold predicts winning 

so basically:
```
riot api -> csv files -> predictions
``` 
with arrows 
- one being this python script 
- and two being weka 
