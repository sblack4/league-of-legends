# results 

## attribute selection on participant frames 
To predict win

```text
=== Run information ===

Evaluator:    weka.attributeSelection.CfsSubsetEval -P 1 -E 1
Search:       weka.attributeSelection.BestFirst -D 1 -N 5
Relation:     participant_frames-weka.filters.unsupervised.attribute.Remove-R11,14-weka.filters.unsupervised.attribute.NumericToNominal-R3-weka.filters.unsupervised.attribute.NumericToNominal-R13
Instances:    19755
Attributes:   13
              pos_x
              pos_y
              win
              creepScore
              currentGold
              dominionScore
              experience
              goldEarned
              level
              neutralMinionsKilled
              teamScore
              timestamp
              match_id
Evaluation mode:    evaluate on all training data



=== Attribute Selection on all input data ===

Search Method:
	Best first.
	Start set: no attributes
	Search direction: forward
	Stale search after 5 node expansions
	Total number of subsets evaluated: 64
	Merit of best subset found:    0.006

Attribute Subset Evaluator (supervised, Class (nominal): 3 win):
	CFS Subset Evaluator
	Including locally predictive attributes

Selected attributes: 5,10 : 2
                     currentGold
                     neutralMinionsKilled
```



## simple kmeans 

```text
=== Run information ===

Scheme:       weka.clusterers.SimpleKMeans -init 0 -max-candidates 100 -periodic-pruning 10000 -min-density 2.0 -t1 -1.25 -t2 -1.0 -N 2 -A "weka.core.EuclideanDistance -R first-last" -I 500 -num-slots 1 -S 10
Relation:     participant_frames-weka.filters.unsupervised.attribute.Remove-R11,14-weka.filters.unsupervised.attribute.NumericToNominal-R3-weka.filters.unsupervised.attribute.NumericToNominal-R13
Instances:    19755
Attributes:   13
              pos_x
              pos_y
              win
              creepScore
              currentGold
              dominionScore
              experience
              goldEarned
              level
              neutralMinionsKilled
              teamScore
              timestamp
              match_id
Test mode:    evaluate on training data


=== Clustering model (full training set) ===


kMeans
======

Number of iterations: 16
Within cluster sum of squared errors: 31766.48577852686

Initial starting points (random):

Cluster 0: 6906,6753,1,10,411,0,4828,5161,8,0,0,480.262,2781987720
Cluster 1: 6029,6151,1,12,900,0,2126,3750,5,0,0,240.168,2766317613

Missing values globally replaced with mean/mode

Final cluster centroids:
                                    Cluster#
Attribute               Full Data          0          1
                        (19755.0)   (9136.0)  (10619.0)
=======================================================
pos_x                   6391.8586  6105.7805  6637.9843
pos_y                   6248.1871  5955.6956  6499.8307
win                             0          0          0
creepScore                 27.515    46.8722    10.8611
currentGold              936.4085  1040.0177   847.2689
dominionScore                   0          0          0
experience              8385.2608 14303.1266  3293.8565
goldEarned              6884.1252 10672.9999   3624.387
level                     10.0832    14.6144     6.1848
neutralMinionsKilled       1.4027      2.388      0.555
teamScore                       0          0          0
timestamp                660.1909  1040.1009   333.3374
match_id               2774503426 2774503426 2766317613




Time taken to build model (full training data) : 0.28 seconds

=== Model and evaluation on training set ===

Clustered Instances

0       9136 ( 46%)
1      10619 ( 54%)

```


## simple kmeans 3 clusters 

```text
=== Run information ===

Scheme:       weka.clusterers.SimpleKMeans -init 0 -max-candidates 100 -periodic-pruning 10000 -min-density 2.0 -t1 -1.25 -t2 -1.0 -N 3 -A "weka.core.EuclideanDistance -R first-last" -I 500 -num-slots 1 -S 10
Relation:     participant_frames-weka.filters.unsupervised.attribute.Remove-R11,14-weka.filters.unsupervised.attribute.NumericToNominal-R3-weka.filters.unsupervised.attribute.NumericToNominal-R13
Instances:    19755
Attributes:   13
              pos_x
              pos_y
              win
              creepScore
              currentGold
              dominionScore
              experience
              goldEarned
              level
              neutralMinionsKilled
              teamScore
              timestamp
              match_id
Test mode:    evaluate on training data


=== Clustering model (full training set) ===


kMeans
======

Number of iterations: 14
Within cluster sum of squared errors: 24082.279111956355

Initial starting points (random):

Cluster 0: 6906,6753,1,10,411,0,4828,5161,8,0,0,480.262,2781987720
Cluster 1: 6029,6151,1,12,900,0,2126,3750,5,0,0,240.168,2766317613
Cluster 2: 4404,4839,0,58,984,0,14519,10784,15,0,0,960.386,2766317613

Missing values globally replaced with mean/mode

Final cluster centroids:
                                    Cluster#
Attribute               Full Data          0          1          2
                        (19755.0)   (4260.0)   (4931.0)  (10564.0)
==================================================================
pos_x                   6391.8586  6158.1669  6659.2367  6361.2911
pos_y                   6248.1871   6018.961   6513.753  6216.6648
win                             0          1          1          0
creepScore                 27.515    47.9385    11.0211    26.9779
currentGold              936.4085  1135.3646   892.0053   876.9045
dominionScore                   0          0          0          0
experience              8385.2608 14806.3002  3333.8698  8153.7936
goldEarned              6884.1252 11076.8038  3692.6374  6683.1043
level                     10.0832    14.8002      6.216     9.9861
neutralMinionsKilled       1.4027      2.684     0.6782     1.2243
teamScore                       0          0          0          0
timestamp                660.1909  1052.8118   332.8618   654.6528
match_id               2774503426 2774503426 2766317613 2756265176




Time taken to build model (full training data) : 0.12 seconds

=== Model and evaluation on training set ===

Clustered Instances

0       4260 ( 22%)
1       4931 ( 25%)
2      10564 ( 53%)


```


## sql tables created

new table:
```sql

drop table match_participant_time;
create table match_participant_time (colPK INTEGER PRIMARY KEY AUTOINCREMENT, pos_x, pos_y, win, currentGold, goldEarned, neutralMinionsKilled);
insert into match_participant_time select 
	null, pos_x, pos_y, win, currentGold, goldEarned, neutralMinionsKilled
from participant_frames
order by match_id, participantId , timestamp;

```