#! python3
# madLibs.py
# Usage: Reads a text file and replaces word types with user input.

import re

# Opens file in read mode and store words into variable
madFile = open(f'madLib.txt', 'r')
words = madFile.read().split()
madFile.close()

# Open result file in write mode
madFile = open(f'madLibResult.txt', 'w')
# Create regex for possible word types
adjReg = re.compile(r'ADJECTIVE')
nounReg = re.compile(r'NOUN')
verbReg = re.compile(r'VERB')

# loop through each word and compare to regex
for word in words:
    if adjReg.match(word):
        word = input("Enter an adjective: ")
    elif nounReg.match(word):
        word = input("Enter a noun: ")
    elif verbReg.match(word):
        word = input("Enter a verb: ")
# Create variable for printing and save to file
    madLibPrint = word + " "
    madFile.write(word + " ")
madFile.close()
