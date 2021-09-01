# -*- coding: utf-8 -*-
"""
CSC 221
M1HW2
Robert Land
9/1/2021
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
    print(temperatures.sort_index(axis=1))
main()
