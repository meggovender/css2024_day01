# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:12:41 2024

@author: megan
"""

import pandas

import pandas as pd

file = pandas.read_csv("C:/Users/megan/CSS2024_DAY_1/.spyproject/country_data.csv")

print(file)

print(file.info())

"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 11 entries, 0 to 10
Data columns (total 3 columns):
 #   Column   Non-Null Count  Dtype 
---  ------   --------------  ----- 
 0   Age      11 non-null     int64 - integer
 1   Gender   11 non-null     object - string
 2   Country  11 non-null     object - string
dtypes: int64(1), object(2)
memory usage: 396.0+ bytes
"""

print(file.describe())

"""
Diab_data set
"""

diab_data = pandas.read_csv("C:/Users/megan/CSS2024_DAY_1/.spyproject/diab_data.csv")

print(diab_data)

print(diab_data.info())

print(diab_data.describe())

"""
Housing_data
"""
housing = pandas.read_csv("C:/Users/megan/CSS2024_DAY_1/.spyproject/housing_data.csv")

print(housing)

column_names = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"]
housing = pandas.read_csv("C:/Users/megan/CSS2024_DAY_1/.spyproject/housing_data.csv", names = column_names)

print(housing.info())

print(housing.describe())

"""
insurance_data
"""
insurance = pandas.read_csv("C:/Users/megan/CSS2024_DAY_1/.spyproject/insurance_data.csv", skiprows = 5)

print(insurance)

print(insurance.info())

print(insurance.describe())

"""
iris_data
"""

iris = pandas.read_csv("C:/Users/megan/CSS2024_DAY_1/.spyproject/iris.csv")

print(iris)

print(iris.info())

print(iris.describe())




