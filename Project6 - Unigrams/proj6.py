"""
Team Member 1: Evan Swanson
Team Member 2: N/A 
GU Username of project lead: eswanson2
Project 6:  This program generates a random sentence using unigrams
Due: 10/26/2018
"""
import nltk
import random

def generateSentence(dictionary, count):
    sentence = ""
    for x in range(0, 10):
        index = float(random.randint(0, count)) / float(count)
        for y in dictionary:
            if dictionary[y][1] > index:
                if x == 0:
                    sentence = sentence + y.capitalize() + " "
                else:
                    sentence = sentence + y + " "
                break 
    sentence = sentence[:-1]
    sentence = sentence + "."
    print sentence

    

def main():
    from nltk.corpus import brown
    tmp = brown.sents(categories = 'editorial')

    new = [[item.encode('ascii') for item in lst] for lst in tmp] #convert to ascii
    new = [[x for x in lst if x != '.' and x != '?' and x != ',' and x != '!' and x != ';' and x != ':' and x != '--'] for lst in new] #remove periods
    new = [[x.lower() for x in lst] for lst in new] #convert all to lowercase

    #find total words
    count = 0
    for x in new:
        count = count + len(x)

    dictionary = {}

    #count each word's occurance
    for x in new:
        for word in x:
            if word in dictionary:
                dictionary[word][0] += 1
            else:
                dictionary[word] = [1,0]

    #calculate each word's relative probability
    for x in dictionary:
        dictionary[x][0] = float(dictionary[x][0]) / float(count)
    
    cumulative = float(0)

    #calculate the cumulative probability
    for x in dictionary:
        cumulative = cumulative + dictionary[x][0]
        dictionary[x][1] = cumulative

    #generate 5 random sentences
    print ""
    for x in range(0,5):
        generateSentence(dictionary, count)
    print ""

main()