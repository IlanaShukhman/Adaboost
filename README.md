# Adaboost

## Submitters:

Ilana Shukhman 211602289

## Python version:

3.8

## Results - HC body temperature

number of rules: 1
train error: 21.45 
test error: 29.94

number of rules: 2
train error: 22.28 
test error: 30.68

number of rules: 3
train error: 17.5 
test error: 30.42

number of rules: 4
train error: 18.07 
test error: 30.54

number of rules: 5
train error: 14.68 
test error: 30.07

number of rules: 6
train error: 15.07 
test error: 30.57

number of rules: 7
train error: 13.23 
test error: 30.56

number of rules: 8
train error: 13.62 
test error: 30.43

### Overfitting?

We can see that, while the train error goes down, the test error stays on 30%, so we can say there is an overfitting. 

## Results - Iris

number of rules: 1
train error: 2.22 test error: 4.9

number of rules: 2
train error: 2.35 test error: 4.98

number of rules: 3
train error: 2.03 test error: 4.85

number of rules: 4
train error: 2.21 test error: 4.93

number of rules: 5
train error: 2.08 test error: 5.02

number of rules: 6
train error: 2.03 test error: 5.07

number of rules: 7
train error: 2.12 test error: 5.23

number of rules: 8
train error: 2.13 test error: 5.14

### Overfitting?

The difference between the train and test error is very small in all the rules, however in the last couple of rules the test error is growing faster. Therefore we can conclude that there is an overfitting, but it is very small. 
