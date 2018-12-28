"""
Team Member 1: Evan Swanson
Team Member 2: N/A 
GU Username of project lead: eswanson2
Test 3C:  This program implements the cyk parser
usage: python cyk.py cfg1.txt strng1.txt
Due: 12/13/2018
"""
import sys

def cyk(cfg, userString):
    #create matrix
    mat = [[[] for x in range(0, len(userString))] for y in range(0, len(userString))]
    #initialize diagonal row
    for i in range(0, len(userString)):
        for LHS in cfg:
            if userString[i] in cfg[LHS]:
                mat[i][i].append(LHS)
    #recursion to fill out matrix
    for step in range(2,len(userString) + 1):
        for i in range(1, len(userString) - step + 2):
            for k in range(i, i + step - 1):
                for LHS in cfg:
                    for pair in cfg[LHS]:
                        if ( len(pair) > 1):
                            if (pair[0] in mat[i - 1][k - 1] and pair[1] in mat[k][i+step-2]) or (pair[1] in mat[i-1][k-1] and pair[0] in mat[k][i+step-2]):
                                mat[i-1][i+step-2].append(LHS)

   

    string = ""
    #ending check and print output
    if 'S' in mat[0][len(userString) - 1]:
        for letter in userString:
            string = string + ' ' + letter
        print string[1:] + ": yes"
    else:
        for letter in userString:
            string = string + ' ' + letter 
        print string[1:] + ": no"






def main():
    cfgFileName = sys.argv[1]
    stringFileName = sys.argv[2]

    #process file into dictionary so LHS are keys and RHS are a list for that key
    cfgFile =  open(cfgFileName, "r")
    cfg = {}
    inputString = cfgFile.read()
    inputLines = inputString.split('\n')
    inputList = [[word for word in line.split(' ')] for line in inputLines]
    for line in inputList:
        LHS = 1
        LHSWord = ""
        for word in line:
            if word == ' ':
                continue
            elif word == ':':
                LHS = 0
            elif LHS:
                cfg[word] = []
                LHSWord = word
            elif word == '|':
                continue
            else:
                cfg[LHSWord].append(word)


        
    cfgFile.close()

    stringFile = open(stringFileName, "r")
    userString = [word for word in stringFile.read().split()]
    stringFile.close()

    cyk(cfg, userString)


main()