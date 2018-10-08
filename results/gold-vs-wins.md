# gold vs wins
The data was collected with `../faker-matches.py` and 
analyzed with Weka 


### n = 100
Basically there is no correlation between the two variables in this set of the last 100 matches by faker


```text
=== Run information ===

Scheme:       weka.classifiers.functions.LinearRegression -S 0 -R 1.0E-8 -additional-stats -output-debug-info -num-decimal-places 40
Relation:     gold-win-weka.filters.unsupervised.attribute.Remove-R1
Instances:    100
Attributes:   2
              win
              gold_earned
Test mode:    evaluate on training data

=== Classifier model (full training set) ===


Linear Regression Model

win =

0.000026401926029239567 * gold_earned +
0.1908379540165253

Regression Analysis:

Variable        Coefficient     SE of Coef        t-Stat
gold_earned   0.000026401926029239567   0.000015027427236288469   1.7569159120919766
const         0.1908379540165253   0.19932435748916358   0.957424152373853

Degrees of freedom = 98
R^2 value = 0.030535687567509684
Adjusted R^2 = 0.02064
F-statistic = 3.0867535227856413

Time taken to build model: 0.01 seconds

=== Evaluation on training set ===

Time taken to test model on training data: 0 seconds

=== Summary ===

Correlation coefficient                  0.1747
Mean absolute error                      0.483 
Root mean squared error                  0.4914
Relative absolute error                 96.9464 %
Root relative squared error             98.4614 %
Total Number of Instances              100     


```


## n = 500
same thing 
```text
=== Run information ===

Scheme:       weka.classifiers.functions.LinearRegression -S 0 -C -R 1.0E-8 -minimal -additional-stats -output-debug-info -num-decimal-places 9
Relation:     gold-win-weka.filters.unsupervised.attribute.Remove-R1
Instances:    500
Attributes:   2
              win
              gold_earned
Test mode:    evaluate on training data

=== Classifier model (full training set) ===

Linear Regression: Model built.

Time taken to build model: 0.01 seconds

=== Evaluation on training set ===

Time taken to test model on training data: 0 seconds

=== Summary ===

Correlation coefficient                  0.209 
Mean absolute error                      0.478 
Root mean squared error                  0.4889
Relative absolute error                 95.6337 %
Root relative squared error             97.7925 %
Total Number of Instances              500  
```