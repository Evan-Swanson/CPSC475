"""
Team Member 1: Evan Swanson
Team Member 2: N/A 
GU Username of project lead: eswanson2
Project 4:  This program implements the Soundex algorithm 
Due: 9/28/2018
"""
import re
import sys

#pre: user entered name as second command line argument
#post: returns the name as a string or displays an error
def getUserWord():
    if len(sys.argv) < 2:
        print("Error: provide name in command line (ex: python proj4.py Jurafsky)")
        exit(1) 
    return sys.argv[1]

#pre: restOfWord is the name without the first letter
#post: returns the word without vowels and h and w
def dropVowels(restOfWord):
    return re.sub('[aehiouwy]', '', restOfWord)

#pre: noVowels is the name without vowels and h and w
#post: returns the coresponding number string
def replaceWithNumbers(noVowels):
    noVowels = re.sub('[bfpv]' , '1', noVowels)
    noVowels = re.sub('[cgjkqsxz]', '2', noVowels)
    noVowels = re.sub('[dt]', '3', noVowels)
    noVowels = re.sub('l', '4', noVowels)
    noVowels = re.sub('[mn]', '5', noVowels)
    noVowels = re.sub('r', '6', noVowels)
    return noVowels

#pre: replacedNumbers is the string of replaced letters
#post: returns the string with repeating adjecent numbers removed
def deleteMultipleNumbers(replacedNumbers):
    return re.sub(r'([0-9])\1+', r'\1', replacedNumbers)

#pre: noDuplicates is a string of numbers with no repeating adjacent
#post: returns a string of 3 numbers, either cutting or padding with 0s
def makeLengthThree(noDuplicates):
    if len(noDuplicates) > 3:
        return noDuplicates[:3]
    elif len(noDuplicates) < 3:
        while len(noDuplicates) != 3:
            noDuplicates = noDuplicates + '0'
    return noDuplicates

def main():
    userWord = getUserWord()
    firstLetter = userWord[0]
    restOfWord = userWord[1:]
    noVowels = dropVowels(restOfWord)
    replacedNumbers = replaceWithNumbers(noVowels)
    noDuplicates = deleteMultipleNumbers(replacedNumbers)
    finalString = firstLetter + makeLengthThree(noDuplicates)
    print(userWord + " -> " + finalString)


    


main()
