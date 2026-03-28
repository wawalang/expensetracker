# Requirements
# Users can add an expense with a description and amount. Users can update an expense. Users can delete an expense. Users can view all expenses. Users can view a summary of all expenses.Users can view a summary of expenses for a specific month (of current year). #

# Additional
# Add expense categories and allow users to filter expenses by category. Allow users to set a budget for each month and show a warning when the user exceeds the budget. Allow users to export expenses to a CSV file.

import argparse, os
from datetime import datetime
from pathlib import Path
parser = argparse.ArgumentParser()
""" parser.add_argument("echo", help="echo the string")
# now the command is like this: x.py [something] -- first argument added is echo, and the commands first argument is something, so it echoes the argument.
args = parser.parse_args()
print(args.echo) """

# HOW IT SHOULD BE
# add - expensetracker.py add --amount [amount] --description [description] ----- creates a number ID for expense.
# remove - expensetracker.py remove [ID]
# update - expensetracker.py update [ID]
# view - expensetracker.py [view] --month:...

parser.add_argument('main', help='put add/remove/view')
parser.add_argument('--amount', help='amount/ID', type=float)
parser.add_argument('--description', help='description')
args: argparse.Namespace = parser.parse_args()

def addE(amount, description):
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
    n.write(f'{amount}\n{description}')
    n.close()
    print(f"Successfully added expense.\nID:{idnum}\nAmount: {amount}\nDescription: {description}")
if args.main == "add":
    addE(args.amount, args.description)
