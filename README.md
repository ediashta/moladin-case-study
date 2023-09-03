# **Moladin Case Study**

## Project Overview

### Background
Moladin provides capital for agents to buy used cars and in return Moladin charges fees (admin fee & aging fee) to agents when the cars are successfully sold. Every car buyout proposal by an agent has to be approved by the branch manager. In order to make an informed decision, the branch manager has to consider several parameters.

## Project Task
As a data scientis we are going to analyze the reason on why some care are selling below target, and create a model to help prevent and mitigate other poor quality buy happen in the future.
There are several steps that will be taken in this project:

1. Analyze the given datasets to gain insight on car buyout quality
2. Perform a regression modeling to predict the car sale price

For the modeling we are going to use 4 base model, which is:
1. Linear Regression
2. Decision Tree
3. Random Forest
4. XGBoost

From these 4 model we are going to choose the best one based on the **MAE** metrics to then perform parameter tuning

## Project Results

Best model achieved is using random forest with this parameter
```
'random_forest__bootstrap': True
'random_forest__max_depth': None
'random_forest__min_samples_leaf': 1
'random_forest__min_samples_split': 2
'random_forest__n_estimators': 100
```
Resulting in MAE Score of 79.9, a relatively small number compared to the car prices

![Random Forest Scatter Plot](./Random%20Forest%20Output.png "Random Forest Scatter Plot")