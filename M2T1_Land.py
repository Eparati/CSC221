# -*- coding: utf-8 -*-
"""
CSC 221
M2T1
Robert Land
9/1/2021
"""
import json
def FileWrite():
    """Write accounts to file"""
    with open('accounts.txt', mode='w') as accounts:
        accounts.write("100 Jones 24.98\n")
        accounts.write("200 Doe 345.67\n")
        accounts.write("300 White 0.00\n")
        accounts.write("400 Stone -42.16\n")
        accounts.write("500 Rich 224.62\n")
def fileRead():
    """Read accounts to file"""
    with open('accounts.txt', mode='r') as accounts:
        print(f'{"Account":<10}{"Name":<10}{"Balance":>10}')
        for record in accounts:
            account, name, balance = record.split()
            print(f'{account:<10}{name:<10}{balance:>10}')
def fileUpdate():
    "Update a single record"
    accounts = (open("accounts.txt","r"))
    tempfile = (open("temp_file.txt","w"))
    with accounts, tempfile:
        for record in accounts:
            account, name, balance = record.split()
            if account != "300":
                tempfile.write(record)
            else:
                new_record = " ".join([account, 'Williams', balance])
                tempfile.write(new_record + "\n")
def jsonWrite():
    accounts_dict= {"accounts": [
        {"account": 100, "name": "Jones", "balance": 24.98},
        {"account": 200, "name": "Doe", "balance": 345.67}
        ]}

    with open("accounts.json","w") as accounts:
        json.dump(accounts_dict, accounts)
def jsonRead():
    with open("accounts.json","r") as accounts:
        accounts_json = json.load(accounts)
        print(accounts_json)
def jsonDisplay():
    with open("accounts.json","r") as accounts:
        print(json.dumps(json.load(accounts),indent =4))
FileWrite()
fileRead()
fileUpdate()
jsonWrite()
jsonRead()
jsonDisplay()