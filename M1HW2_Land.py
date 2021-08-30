# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 13:51:59 2021

@author: landr3615
"""

"""
a)create dataframe "temperatures" with readings for maxine, james, and amanda
b)remake df temps in a with custom indices using index
c) select from temps of maxine
d)select from row mornings
e)select from row morning and evening
f)select from amanda and maxine
g)select from " " " in morning and afternoon
h)use describe method on temperatures
i)transpose temperatures
j)sort temperatures so column names in alphabetical order
"""
import pandas as pd
def main():
    temperatures_dict = {"Maxine": [87, 96,93], "James": [100,87,90], "Amanda":[97,89,106]}
    temperatures = pd.DataFrame(temperatures_dict)
    temperatures.index = ["Morning", "Evening", "Afternoon"]
    print("The following are temperatures for Maxine: ")
    print(temperatures.loc[:,"Maxine"],"\n")
    print("The following are temperatures for the morning: ")
    print(temperatures.loc["Morning"],"\n")
    print("The following are temperatures for the morning and evening:")
    print(temperatures.loc["Morning":"Evening"],"\n")
    print("The following are temperatures for Amanda and Maxine:")
    print(temperatures.loc[:,["Amanda","Maxine"]],"\n")
    print("The following are temperatures for Amanda and Maxine during the morning and afternoon:")
    print(temperatures.loc[["Morning","Afternoon"],["Amanda","Maxine"]],"\n")
    print("The following describes the temperatures data frame:")
    print(temperatures.describe(),"\n")
    print("The following will be a transpose of the temperatures Data Frame:")
    print(temperatures.T,"\n")
    print("The following is a sorted form of temperatures where each column will be in alphabetical order.")
    
main()