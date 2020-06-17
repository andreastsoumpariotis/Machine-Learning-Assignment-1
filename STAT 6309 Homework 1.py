#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 17:58:09 2020

@author: andreastsoumpariotis
"""

# Question 8
import pandas as pd

# Part a
college = pd.read_csv('College.csv')
college

# part b
college = college.rename(columns = {"Unnamed: 0":"row.names"})

# part c

# i
numerical = college.describe
print(numerical)
pd.set_option('display.max_rows', None)

# ii
import seaborn as sns
sns.pairplot(college)

# iii
Private = college['Private']
Outstate = college['Outstate']
sns.boxplot(x = Private, y = Outstate)

# iv
Top10perc = college["Top10perc"]
Elite_All = college[Top10perc > 50]
Top10perc = Top10perc[Top10perc <= 50] = "No"
Top10perc = Top10perc[Top10perc > 50] = "Yes"
Elite = Elite_All["Top10perc"]
len(Elite_All) #78 elite universities

# Boxplot of Outstate vs Elite
x = [Top10perc > 50]
x = pd.DataFrame(x) 
college.insert(1, "Above50", x)
college["Above50perc"]
sns.boxplot(x = x, y = Outstate)

college["Top10perc"] = college["Top10perc"].astype("category")

# v
import matplotlib.pyplot as plt

plt.ylabel = "Frequency"
plt.xlabel = "Costs"

Room = college['Room.Board']
Room.plot.hist(Room, bins=30)
plt.title('Histogram of Room/Board Costs')
plt.ylabel('Frequency')
plt.xlabel('Costs')

Outstate = college['Outstate']
Outstate.plot.hist(Outstate, bins=30)
plt.title('Histogram of Outstate Costs')
plt.xlabel('Costs')
plt.ylabel = ('Frequency')

Grad = college['Grad.Rate']
Grad.plot.hist(Grad, bins=30)
plt.title('Histogram of Graduate Costs')
plt.xlabel('Rate')
plt.ylabel = ('Frequency')

# Question 9
auto = read.csv('Auto.csv')

# part a
# Quantitative: mpg, cylinders, displacement, horsepower, weight, acceleration, 
# year and origin
# Qualitative: name

# part b
mpg = auto['mpg']
min(mpg) #9
max(mpg) #46

cylinder = auto['cylinders']
min(cylinder) #3
max(cylinder) #8

displacement = auto['displacement']
min(displacement) #68
max(displacement) #455

horsepower = auto['horsepower']
min(horsepower) #46
max(horsepower) #230

weight = auto['weight']
min(weight) #1613
max(weight) #5140

acceleration = auto['acceleration']
min(acceleration) #8
max(acceleration) #24.8

year = auto['year']
min(year) #70
max(year) #82

origin = auto['origin']
min(origin) #1
max(origin) #3

# part c
from statistics import stdev
from statistics import mean

mean(mpg) #23.51586901763224
stdev(mpg) #7.825803928946562

mean(cylinder) #5.458438287153652
stdev(cylinder) #1.7015769807918462

mean(displacement) #193.53274559193954
stdev(displacement) #104.37958329992955

mean(horsepower) #104.4694
stdev(horsepower) #38.49116

mean(weight) #2970.2619647355164
stdev(weight) #847.9041194897246

mean(acceleration) #15.55566750629723
stdev(acceleration) #2.749995292976151

mean(year) #75.99496221662469
stdev(year) #3.690004901461682

mean(origin) #1.5743073047858942
stdev(origin) #0.8025494957970388

# part d

new_auto = auto.drop([10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85], axis = 0)

mpg = new_auto['mpg']
min(mpg) #11
max(mpg) #46.6
mean(mpg) #24.44485981308411
stdev(mpg) #7.8999276141247785

cylinder = new_auto['cylinders']
min(cylinder) #3
max(cylinder) #8
mean(cylinder) #5.370716510903427
stdev(cylinder) #1.6534856508321407

displacement = new_auto['displacement']
min(displacement) #68
max(displacement) #455
mean(displacement) #187.17445482866043
stdev(displacement) #99.86456814308559

horsepower = new_auto['horsepower']
min(horsepower) #46
max(horsepower) #230
mean(horsepower) #100.9558
stdev(horsepower) #35.89557

weight = new_auto['weight']
min(weight) #1613
max(weight) #5140
mean(weight) #2933.183800623053
stdev(weight) #809.6386504094033

acceleration = new_auto['acceleration']
min(acceleration) #8.5
max(acceleration) #24.8
mean(acceleration) #15.709034267912772
stdev(acceleration) #2.70644127535534

year = new_auto['year']
min(year) #70
max(year) #82
mean(year) #77.14330218068535
stdev(year) #3.128202408976516


origin = new_auto['origin']
min(origin) #1
max(origin) #3
mean(origin) #1.5981308411214954
stdev(origin) #0.8161626647471096

# part e

# plot 1
plt.scatter(weight, mpg)
plt.title('MPG vs. Weight')
plt.ylabel('Miles Per Gallon')
plt.xlabel('Car Weight')

# plot 2
plt.scatter(weight, acceleration)
plt.title('Car Acceleration vs. Weight')
plt.ylabel('Car Acceleration')
plt.xlabel('Weight')

# plot 3
plt.scatter(acceleration, displacement)
plt.title('Car Displacement vs. Acceleration')
plt.ylabel('Displacement')
plt.xlabel('Acceleration')

# part f

plt.scatter(cylinder, mpg)
plt.title('MPG vs. Cylinder')
plt.ylabel('Miles Per Gallon')
plt.xlabel('Cylinder Amount')

plt.scatter(displacement, mpg)
plt.title('MPG vs. Displacement')
plt.ylabel('Miles Per Gallon')
plt.xlabel('Displacement')

plt.scatter(weight, mpg)
plt.title('MPG vs. Weight')
plt.ylabel('Miles Per Gallon')
plt.xlabel('Car Weight')

plt.scatter(acceleration, mpg)
plt.title('MPG vs. Acceleration')
plt.ylabel('Miles Per Gallon')
plt.xlabel('Acceleration')

plt.scatter(year, mpg)
plt.title('MPG vs. Year')
plt.ylabel('Miles Per Gallon')
plt.xlabel('Year')

plt.scatter(origin, mpg)
plt.title('MPG vs. Origin')
plt.ylabel('Miles Per Gallon')
plt.xlabel('Origin')

# Question 10

# part a
boston = pd.read_csv('Boston.csv')
boston
# 14 columns (variables/predictors) and 506 rows (observations)

# part b
crim = boston['crim']
zn = boston['zn']
indus = boston['indus']
chas = boston['chas']
nox = boston['nox']
rm = boston['rm']
age = boston['age']
dis = boston['dis']
rad = boston['rad']
tax = boston['tax']
ptratio = boston['ptratio']
black = boston['black']
lstat = boston['lstat']
medv = boston['medv']

# Crime Rate vs Nitrogen Oxide Concentration
plt.scatter(nox, crim)
plt.title('Crime Rate vs Nitrogen Oxide Concentration')
plt.ylabel('Crime Rate')
plt.xlabel('Nitrogen Oxide Concentratio (parts per 10 million)')

# Taxes vs Pupil-Teacher Ratio
plt.scatter(ptratio, tax)
plt.title('Taxes vs Pupil-Teacher Ratio')
plt.ylabel('Taxes')
plt.xlabel('Pupil-Teacher Ratio')

# Percent of Lower Status Population vs Average Number of Rooms per Dwelling
plt.scatter(rm, lstat)
plt.title('Percent of Lower Status Population vs Average Number of Rooms per Dwelling')
plt.ylabel('Percent of Lower Status Population')
plt.xlabel('Average Number of Rooms per Dwelling')

# Crime Rate vs Percent of Lower Status Population
plt.scatter(lstat, crim)
plt.title('Crime Rate vs Percent of Lower Status Population')
plt.ylabel('Crime Rate')
plt.xlabel('Percent of Lower Status Population')

# part c

# Crime Rate vs Proportion of residential land zoned for lots over 25,000 sq.ft.
plt.scatter(zn, crim)
plt.title('Crime Rate vs Proportion of Residential Land Zoned for Lots over 25,000 sq ft')
plt.ylabel('Crime Rate')
plt.xlabel('Proportion of Residential Land')

# Crime Rate vs Proportion of Non-Retail Business Acres per Town
plt.scatter(indus, crim)
plt.title('Crime Rate vs Proportion of Non-Retail Business Acres per Town')
plt.ylabel('Crime Rate')
plt.xlabel('Proportion of Non-Retail Business Acres per Town')

# Crime Rate vs Charles River Vicinity
plt.scatter(chas, crim)
plt.title('Crime Rate vs Charles River Vicinity')
plt.ylabel('Crime Rate')
plt.xlabel('Charles River Vicinity')

# Crime Rate vs Nitrogen Oxide Concentration
plt.scatter(nox, crim)
plt.title('Crime Rate vs Nitrogen Oxide Concentration')
plt.ylabel('Crime Rate')
plt.xlabel('Nitrogen Oxide Concentratio (parts per 10 million)')
#(Question 10b Plot 1)

# Crime Rate vs Average Number of Rooms per Dwelling
plt.scatter(rm, crim)
plt.title('Crime Rate vs Average Number of Rooms per Dwelling')
plt.ylabel('Crime Rate')
plt.xlabel('Average Number of Rooms per Dwelling')

# Crime Rate vs Proportion of Owner-Occupied Units Built Prior to 1940
plt.scatter(age, crim)
plt.title('Crime Rate vs Proportion of Owner-Occupied Units Built Prior to 1940')
plt.ylabel('Crime Rate')
plt.xlabel('Proportion of Owner-Occupied Units Built Prior to 1940')

# Crime Rate vs Weighted Mean of Distances to Five Boston Employment Centers
plt.scatter(dis, crim)
plt.title('Crime Rate vs Weighted Mean of Distances to Five Boston Employment Centers')
plt.ylabel('Crime Rate')
plt.xlabel('Weighted Mean of Distances')

# Crime Rate vs Index of Accessibility to Radial Highways
plt.scatter(rad, crim)
plt.title('Crime Rate vs Index of Accessibility to Radial Highways')
plt.ylabel('Crime Rate')
plt.xlabel('Index of Accessibility to Radial Highways')

# Crime Rate vs Full Value Property Tax Rate (per $10,000)
plt.scatter(tax, crim)
plt.title('Crime Rate vs Full Value Property Tax Rate (per $10,000)')
plt.ylabel('Crime Rate')
plt.xlabel('Tax Rate')

# Crime Rate vs Pupil-Teacher Ratio
plt.scatter(ptratio, crim)
plt.title('Crime Rate vs Pupil-Teacher Ratio')
plt.ylabel('Crime Rate')
plt.xlabel('Pupil-Teacher Ratio')

# Crime Rate vs Proportion of Blacks by Town
plt.scatter(black, crim)
plt.title('Crime Rate vs Proportion of Blacks by Town')
plt.ylabel('Crime Rate')
plt.xlabel('Proportion of Blacks')

# Crime Rate vs Percent of Lower Status Population
plt.scatter(lstat, crim)
plt.title('Crime Rate vs Percent of Lower Status Population')
plt.ylabel('Crime Rate')
plt.xlabel('Percent of Lower Status Population')
#(Question 10b Plot 4)

# Crime Rate vs Median Value of Owner-Occupied Homes (in $1000s)
plt.scatter(black, crim)
plt.title('Crime Rate vs Median Value of Owner-Occupied Homes (in $1000s)')
plt.ylabel('Crime Rate')
plt.xlabel('Median Value')

# part d

# Crime
min(crim) #0.00632
max(crim) #88.9762

# Zn
min(zn) #0
max(zn) #100

# Indus
min(indus) #0.46
max(indus) #27.74

# Chas
min(chas) #0
max(chas) #1

# nox
min(nox) #0.385
max(nox) #0.871

# rm
min(rm) #3.5610000000000004
max(rm) #8.78

# age
min(age) #2.9
max(age) #100

# dis
min(dis) #1.1296
max(dis) #12.1265

# rad
min(rad) #1
max(rad) #24

# tax
min(tax) #187
max(tax) #711

# ptratio
min(ptratio) #12.6
max(ptratio) #22.0

# black
min(black) #0.32
max(black) #396.9

# lstat
min(lstat) #1.73
max(lstat) #37.97

# medv
min(medv) #5
max(medv) #50

# part e
sum(chas == 1) #35 by Charles River

# part f
from statistics import *
median(ptratio) #19.05

# part g
min(medv) #5
m = boston[medv == min(medv)]

# part h
sum(rm > 7) #64 avg more than 7 rooms per dwelling
sum(rm > 8) #13 avg more than 8 rooms per dwelling


rm = rm[rm > 8]

crim.loc[97]
crim.loc[163]
crim.loc[204]
crim.loc[224]
crim.loc[225]
crim.loc[226]
crim.loc[232]
crim.loc[233]
crim.loc[253]
crim.loc[257]
crim.loc[262]
crim.loc[267]
crim.loc[364]

A = [[0.12082999999999999, 1.51902, 0.02009, 0.31533, 0.52693, 0.38214000000000004, 0.57529, 0.33147, 0.36894, 0.61154, 0.5201399999999999, 0.57834, 3.4742800000000003]]
# A is made up of the 13 crime rates that correspond with the 13 suburbs that avg more
# than 8 rooms per dwelling

# Crime Rate vs Average Number of Rooms per Dwelling (of sample)
plt.scatter(rm, A)
plt.title('Crime Rate vs Average Number of Rooms per Dwelling')
plt.ylabel('Crime Rate')
plt.xlabel('Average Number of Rooms per Dwelling')

