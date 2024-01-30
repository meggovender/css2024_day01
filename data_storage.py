# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:41:13 2024

@author: megan
"""

"""
Storing data in python
1. Lists
2. Dictionaries
3. Data frames - specific to pandas
"""

import pandas

file = pandas.read_csv("C:/Users/megan/CSS2024_DAY_1/.spyproject/country_data.csv")

print(file)

"""
    Age Gender       Country
0    39      M  South Africa
1    25      M      Botswana
2    29      F  South Africa
3    46      M  South Africa
4    22      F         Kenya
5    35      F    Mozambique
6    22      F       Lesotho
7    49      M         Kenya
8    30      M         Kenya
9    40      F         Egypt
10   30      M         Sudan
"""

age = [30, 25, 29, 46, 22,35, 22, 49, 30, 40, 30]

print(age)

"""
access individual values of a list
"""

print(age[0])

print(age[1])

print(min(age))

print(max(age))

print(sum(age))

print(len(age))

print(sum(age)/len(age))

gender = ["M", "F", "M"]

country_list = ["South Africa"]

print(age[0:2])

age.append(100)

print(age)

age.insert(0,100)

"""
Dictionaries - key: value pairs

cat: "a cute animal"

- unordered 
"""

mammals = {"cat":"a cute animal", "lion": "a big cat", "elephant": "a wise animal"}

print(mammals["cat"])

"""
Data frames

- 2 dimensional
- df = dataframe
"""

fruits = ["apple", "banana", "orange", "grape", "kiwi"]

size_nm = [9.8, 10.1, 13.2, 8.7, 20.5]

fruit_sizes = {'fruit': fruits, 'sizes': size_nm}

df = pandas.DataFrame(fruit_sizes)

print(df["fruit"])
print(df["sizes"])
print(df["sizes"].min())
print(df["sizes"].mean())
print(df.describe())
print(df[df["sizes"]>10])
print(df[1:3])

prices = [10.00, 12.50, 16.00, 23.00, 7.00]

df['prices'] = prices

df.drop(columns =["sizes"], inplace = True)


