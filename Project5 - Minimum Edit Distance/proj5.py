"""
Team Member 1: Evan Swanson
Team Member 2: N/A 
GU Username of project lead: eswanson2
Project 5:  This program computes the minimum edit distance
            between 2 words and displays the necessary changes
Due: 10/5/2018
"""
import sys

#pre: user entered source word as second command line argument
#post: returns the word as a string or displays an error
def getSource():
    if len(sys.argv) < 3:
        print("Error: provide words in command line (ex: python proj5.py box fox)")
        exit(1) 
    return sys.argv[1]

#pre: user entered target word as third command line argument
#post: returns the name as a string or displays an error
def getTarget():
    if len(sys.argv) < 3:
        print("Error: provide words in command line (ex: python proj5.py box fox)")
        exit(1) 
    return sys.argv[2]

#pre: i and j are the current indicies of target and source respectively
#post: returns 0 if they are the same letter, else returns 2
def subCost(source, target, i, j):
    if target[j-1] == source[i-1]:
        return 0
    else:
        return 2

#pre: source and target have been assigned
#post: displays the necessary alignment and returns the min edit distance
def minEditDistance(source, target):
    n = len(target)
    m = len(source)

    #2d array to hold the 'pointer' information
    pointers = [[0 for x in range (n+1)] for y in range(m+1)]
    for column in range(1,m+1):
        pointers[column][0] = 'd'
    for row in range(1,n+1):
        pointers[0][row] = 'l'

    #2d array to hold the min edit distance numbers 
    distance = [[0 for x in range (n+1)] for y in range(m+1)]
    for column in range(1,m+1):
        distance[column][0] = distance[column-1][0] + 1
    for row in range(1,n+1):
        distance[0][row] = distance[0][row-1] + 1

    for i in range(1, m+1):
        for j in range(1, n+1):
            distance[i][j] = min(distance[i-1][j] + 1, 
                                distance[i-1][j-1] + subCost(source, target, i, j),
                                distance[i][j-1] + 1)
            #create "pointer" based on where it came from
            #(e = same letter, s = substitute, d = delete, l = insert)
            #points diagonal
            if distance[i-1][j-1] + subCost(source, target, i, j) == min(distance[i-1][j] + 1, 
                        distance[i-1][j-1] + subCost(source, target, i, j),
                        distance[i][j-1] + 1):
                pointers[i][j] = 's'
            #points down
            elif distance[i-1][j] + 1 == min(distance[i-1][j] + 1, 
                        distance[i-1][j-1] + subCost(source, target, i, j),
                        distance[i][j-1] + 1):
                pointers[i][j] = 'd'
            #points left
            else:
                pointers[i][j] = 'l'
            #points diagonal but was same character
            if subCost(source, target, i, j) == 0:
                pointers[i][j] = 'e'

    i = len(source)
    j = len(target)
    alignSource = ""
    alignTarget = ""
    alignOperations = ""
    nextLetter = 0

    #step backwards through pointer array to creat alignment strings
    while (i + j != 0):
        if pointers[i][j] == 'l':
            alignSource =  '*' + alignSource
            alignTarget = target[j - 1] + alignTarget
            alignOperations = 'i' + alignOperations
            j -= 1

        elif pointers[i][j] == 'd':
            alignSource =  source[i - 1] + alignSource
            alignTarget = '*' + alignTarget
            i -= 1
            alignOperations = 'd' + alignOperations

        else:
            alignSource = source[i - 1] +  alignSource
            alignTarget = target[j - 1] + alignTarget
            if pointers[i][j] == 'e':
                alignOperations = ' ' + alignOperations
            else:
                alignOperations = 's' + alignOperations
            i = i - 1
            j = j - 1

    #display alignment
    print "\n" , alignSource
    print alignTarget
    print alignOperations, "\n"

    return distance[m][n]


def main():
    sourceWord = getSource()
    targetWord = getTarget()
    minDistance = minEditDistance(sourceWord, targetWord)
    print "Minimum Edit Distance: %d" % minDistance , "\n"

main()