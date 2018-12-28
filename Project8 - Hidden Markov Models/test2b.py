"""
Team Member 1: Evan Swanson
Team Member 2: N/A 
GU Username of project lead: eswanson2
Test 2B:  This program implements the Viterbi algorithm
Usage: python test2b.py matA.txt matB.txt 313
Due: 11/30/2018
"""
import sys
import re

def viterbi(aMatrix, bMatrix, userString):
    numStates = len(aMatrix[0]) - 2
    foward = [[0.0 for x in range(0,len(userString))] for y in range(0, numStates)]
    backpointers = [[0 for x in range(0,len(userString) + 1)] for y in range(0, numStates)]
    probability = float(0)
    lastmax = 0
    endState = 0

    #initialize first column
    for row in range(0,numStates):
        foward[row][0] = aMatrix[0][row + 1] * bMatrix[row + 1][(ord(userString[0]) - 49)]
    
    #recursion
    #for each column
    for column in range(1, len(userString)):
        #for each cell in that column
        for row in range(0,numStates):
            #for each path from the previous states
            lastmax = 0
            for backRow in range(0, numStates):
                lastmax = max(lastmax, foward[backRow][column - 1] * aMatrix[backRow + 1][row + 1] * bMatrix[row + 1][(ord(userString[column]) - 49)])
            foward[row][column] = lastmax         
            #backpointer
            for backRow in range(0, numStates):
                if lastmax == foward[backRow][column - 1] * aMatrix[backRow + 1][row + 1] * bMatrix[row + 1][(ord(userString[column]) - 49)]:
                    backpointers[row][column] = backRow
                    break

    lastmax = 0
    #termination
    for row in range(0,numStates):
        lastmax = max(lastmax, foward[row][len(userString) - 1] * aMatrix[row + 1][numStates + 1])

    #from last state to end state    
    for row in range(0, numStates):
                if lastmax == foward[row][len(userString) - 1] * aMatrix[row + 1][numStates + 1]:
                    endState = row
                    break

    #start string with last state
    hiddenString = ""
    hiddenString += chr(endState + 48)

    #follow backpointers back to the start
    nextState = endState
    for column in range(len(userString) - 1, 0, -1):
        hiddenString += chr(backpointers[nextState][column] + 48)
        nextState = backpointers[nextState][column]

    hiddenString = re.sub('1', 'H', hiddenString)
    hiddenString = re.sub('0', 'C', hiddenString)

    #reverse the string so its in correct order
    hiddenString = hiddenString[::-1]
    
    print hiddenString


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

    viterbi(aMatrix, bMatrix, userString)

main()