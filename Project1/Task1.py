"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

# inputs list of calls
# int
# examples [[2343,2345, 66, 77],[2311,2343,555,65]] 3
#
# tracking index
# take first number and compare to each number in the record and add an incrent duplicate each time a duplicate is found
# get the lenght of list multiply by two
# subtract the number of duplicates
# return total

test = [[2343,2345, 66, 77],[2311,2343,555,65]]

def unique_numbers(list):
    iterator = 0
    duplicates = 0

    for i in list:
        for j in i:
            if j


    print(duplicates)


unique_numbers(test)
