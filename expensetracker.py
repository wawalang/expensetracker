# Requirements
# Users can add an expense with a description and amount. Users can update an expense. Users can delete an expense. Users can view all expenses. Users can view a summary of all expenses.Users can view a summary of expenses for a specific month (of current year). #

# Additional
# Add expense categories and allow users to filter expenses by category. Allow users to set a budget for each month and show a warning when the user exceeds the budget. Allow users to export expenses to a CSV file.

import argparse, os
from datetime import datetime
from pathlib import Path
""" parser.add_argument("echo", help="echo the string")
# now the command is like this: x.py [something] -- first argument added is echo, and the commands first argument is something, so it echoes the argument.
args = parser.parse_args()
print(args.echo) """

# HOW IT SHOULD BE
# add - expensetracker.py add --amount [amount] --description [description] ----- creates a number ID for expense.
# remove - expensetracker.py remove [ID]
# update - expensetracker.py update [ID]
# view - expensetracker.py [view] --month:...
parser = argparse.ArgumentParser()
parser.add_argument('main', help='put add/delete/list/summary here. delete can be changed to remove and list can be changed to view.')
parser.add_argument('-a','--amount', help='amount on add, ID on remove and update.', type=float)
parser.add_argument('-d','--description', help='description')
parser.add_argument('-u','--uamount', help="if you're using update, use this as the amount. -a should be ID if you're using update.", type=float)
parser.add_argument('-m','--month', help="(for view) only view a certain month (numeric value) - by default this is 0, which means all months.", type=int)
args: argparse.Namespace = parser.parse_args()
dateNtime=datetime.now()
nyear=dateNtime.year # now year
nmonth=dateNtime.month # now month
nday=dateNtime.day # now day
onlydate=f"{nyear}-{nmonth}-{nday}"
""" EXPENSE FILE FORMAT:
amount
description
date_year
date_month
date_day
"""
def addE(amount, description): # add an expense
    if os.path.exists("IDTrack"):
        with open("IDTrack", "r") as idt:
            idnum = int(idt.read()) + 1
        with open("IDTrack", "w") as idt:
            idt.write(str(idnum))
    else:
        with open("IDTrack", "w") as idt:
            idnum=1
            idt.write(str("1"))
    n = open(str(idnum), "w")
    n.write(f'{amount}\n{description}\n{nyear}\n{nmonth}\n{nday}')
    n.close()
    print(f"Expense added successfully. (ID: {idnum})")
def removeE(ID): # remove an expense
    os.remove(str(int(ID)))
def updateE(ID, amount, description): #update an expense
    with open(str(int(ID)), "w") as fil:
        fil.write(f'{amount}\n{description}\n{nyear}\n{nmonth}\n{nday}')
    print(f"Expense updated successfully. (ID: {ID})")
def viewE(): # view/list expenses (no summary)
    directory=Path('')
    print("-Expense List-")
    for fn in directory.iterdir():
        if fn.name == "IDTrack" or fn.name == "expensetracker.py":
            continue
        with open(fn) as filen:
            amou=filen.readline().strip()
            desc=filen.readline().strip()
            ye=filen.readline().strip()
            mo=filen.readline().strip()
            da=filen.readline().strip()
            combd=f"{ye}-{mo}-{da}"
            print(f"- ID: {fn} - Date: {combd} - Description: {desc} - Amount: {amou}")
    print("--*Finished*--")
def sumE(month=0): # wooow summary oooo waowwww haha hihi.. month includation
    directory = Path('')
    summm = 0
    if month==0:
        for fn in directory.iterdir():
            if fn.name == "IDTrack" or fn.name == "expensetracker.py":
                continue
            with open(fn) as filen:
                amou = float(filen.readline().strip())
                summm += amou
    else:
        for fn in directory.iterdir():
            if fn.name == "IDTrack" or fn.name == "expensetracker.py":
                continue
            with open(fn) as filen:
                amou = float(filen.readline().strip())
                filen.readline()
                year=int(filen.readline()).strip()
                monthf=int(filen.readline()).strip()
            if year==nyear and monthf==month:
                summm += amou
            else:
                continue
    print(f"Total expenses: ${summm}")
    return summm
if args.main == "add":
    addE(args.amount, args.description)
elif args.main == "remove" or args.main == "delete":
    removeE(args.amount)
elif args.main == args.main == "update":
    updateE(args.amount, args.uamount, args.description)
elif args.main == "list" or args.main == "view":
    viewE()
elif args.main == "summary":
    if args.month:
        sumE(args.month)
    else:
        sumE()
