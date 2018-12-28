"""
Team Member 1: Evan Swanson
Team Member 2: N/A 
GU Username of project lead: eswanson2
Project 2: This project allows the user to input a file and find how many instances
           of a word they choose appears in the document
Due: 9/7/2018
"""

import re

def openFile():
    while(True):
        inputFile = raw_input('Enter an input file name:\n')
        try:
            inputFile = open(inputFile, 'r')
            break
        except:
            print("Invalid file name.  Try again.")
    return inputFile

#pre: fin is an opened input file
#post: returns the file as a string that is all lowercase and only spaces before and after words
def read_file_as_string(fin):
    string = fin.read()
    string = string.replace('\n', ' ')
    string = ' ' + string + ' '
    string = string.lower()
    return string

#post: returns a string that is all lowercase with a space before and after
def getWord():
   inputWord = raw_input("Enter the word you wish to count:\n")
   inputWord = ' ' + inputWord + ' '
   inputWord = inputWord.lower()
   return inputWord

def main():
   inputFile = openFile()
   inputString = read_file_as_string(inputFile)
   matches = re.findall(getWord(),inputString)
   print len(matches)
  
main()
