# -*- coding: utf-8 -*-
"""
CSC 221
M1Lab1
Robert Land
8/18/2021
"""
results = [] #global list
def main():
    #main loop
    repeat=True
    while repeat == True:
        collectUserInput()
        repeat = repeatOrNot()
    print("Goodbye.")
    print(results)
def collectUserInput():
    num=int(input("Enter a number: "))
    dbl = doubleANum(num)
    results.append(dbl)
    print(num," doubled is: ", dbl)
def repeatOrNot():
    print("1. Enter another number.")
    print("2. Exit")
    goAgain = int(input())
    if 1 == goAgain:
        return True
    return False
def doubleANum(num):
    result = num * 2
    return result
if __name__ == "__main__":
    main()