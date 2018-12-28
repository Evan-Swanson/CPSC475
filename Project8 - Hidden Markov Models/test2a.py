"""
Team Member 1: Evan Swanson
Team Member 2: N/A 
GU Username of project lead: eswanson2
Test 2A:  This program implements the foward algorithm
Due: 11/20/2018
"""
import sys
import re

def foward(aMatrix, bMatrix, userString):
    numStates = len(aMatrix[0]) - 2
    foward = [[0.0 for x in range(0,len(userString))] for y in range(0, numStates)]
    probability = float(0)

    #initialize first column
    for row in range(0,numStates):
        foward[row][0] = aMatrix[0][row + 1] * bMatrix[row + 1][(ord(userString[0]) - 49)]
    
    #recursion
    #for each column
    for column in range(1, len(userString)):
        #for each cell in that column
        for row in range(0,numStates):
            #for each path from the previous states
            for backRow in range(0, numStates):
                foward[row][column] += foward[backRow][column - 1] * aMatrix[backRow + 1][row + 1] * bMatrix[row + 1][(ord(userString[column]) - 49)]


    #termination
    for row in range(0,numStates):
        probability += foward[row][len(userString) - 1] * aMatrix[row + 1][numStates + 1]

    print "The probability of " + userString + " is: %.6f" % (probability)


def main():
    matAFile = sys.argv[1]
    matBFile = sys.argv[2]

    aFile =  open(matAFile, "r")
    aMatrix = [[float(num) for num in line.split(',')] for line in aFile]
    aFile.close()

    bFile = open(matBFile, "r")
    bMatrix = [[float(num) for num in line.split(',')] for line in bFile]
    bFile.close()
    
    userString = ""
    
    for x in range(3, len(sys.argv)):
        userString += sys.argv[x]

    foward(aMatrix, bMatrix, userString)

main()