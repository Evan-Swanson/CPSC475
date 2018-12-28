"""
Team Member 1: Evan Swanson
Team Member 2: N/A 
GU Username of project lead: eswanson2
Project 7b:  This program generates a random sentence using unigrams, 
            bigrams, trigrams, and quadgrams based off of Shakespeare's
            entire collection of work
Due: 11/2/2018
"""
import re
import random
import pickle
import time

#bogensberg-johnson method
def generateSentence(dictionary, count):
    sentence = ""
    for x in range(0, 12):
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

def generateBigramSentence(dictionary):
    sentence = ""
    nextWord = "<s>"    #must start with beginning sentence marker
    
    for x in range(0, 12):
        numWords = dictionary[nextWord][1] #number of words that start with condition word
        index = float(random.randint(0, numWords)) / float(numWords)
        for z in dictionary[nextWord][0]: #look at the entires in the conditioning word's dict
            if dictionary[nextWord][0][z][1] > index and z != "</s>":
                currentWord = nextWord  
                nextWord = z      #set the condition word for the next pass
                sentence += " "+ currentWord
                break 

    sentence = sentence[5:].capitalize()
    sentence = sentence + "."
    print sentence

def generateTrigramSentence(dictionary):
    sentence = ""
    nextWord = ""
    
    for x in range(0, 13):
        if x == 0:
            while(not nextWord.startswith("<s>")):
                nextWord = random.choice(dictionary.keys())
        
        numWords = dictionary[nextWord][1]
        index = float(random.randint(0, numWords)) / float(numWords)
        for z in dictionary[nextWord][0]:
            if dictionary[nextWord][0][z][1] > index and z != "</s>":
                currentWord = nextWord
                temp = nextWord.split()
                nextWord =  temp[1] + " " + z
                sentence += " "+ currentWord.split()[0]
                break

    sentence += " " + nextWord
    sentence = sentence[5:].capitalize()
    sentence = sentence + "."
    if len(sentence.split()) > 11:
        print sentence
        return 1
    #if it encounterd a </s> with no other options before reaching 12 words, throw it out
    else:
        return 0



def generateQuadgramSentence(dictionary):
    sentence = ""
    nextWord = ""
    
    for x in range(0, 13):
        if x == 0:
            while(not nextWord.startswith("<s>")):
                nextWord = random.choice(dictionary.keys())
        
        numWords = dictionary[nextWord][1]
        index = float(random.randint(0, numWords)) / float(numWords)
        for z in dictionary[nextWord][0]:
            if dictionary[nextWord][0][z][1] > index and z != "</s>":
                currentWord = nextWord
                temp = nextWord.split()
                nextWord =  temp[1] + " " + temp[2] + " " + z
                sentence += " "+ currentWord.split()[0]
                break

    sentence += " " + nextWord
    sentence = sentence[5:].capitalize()
    sentence = sentence + "."
    if len(sentence.split()) > 9:
        print sentence
        return 1
    else:
        return 0

#pickle/depickling makes dictionary entries out of order, so must calc
#cumulative probabilites here so they are sorted
def calcUnigramCumulative(unigrams):
    cumulative = float(0)
    for x in unigrams:
        cumulative = cumulative + unigrams[x][0]
        unigrams[x][1] = cumulative

def calcMultigramCumulative(dictionary):
    for x in dictionary:
        cumulative = float(0)
        for y in dictionary[x][0]:
            cumulative += dictionary[x][0][y][0]
            dictionary[x][0][y][1] = cumulative

    

def deserialize():
    fin = open('proj7.pkl', 'rb')
    lsts_in = pickle.load(fin)
    fin.close()
    return lsts_in

def main():
    random.seed(time.time())
    print "Depickle takes a second..."
    masterList = deserialize()

    unigrams = masterList[1]
    bigrams = masterList[2]
    trigrams = masterList[3]
    quadgrams = masterList[4]

    #unigrams
    calcUnigramCumulative(unigrams)
    print "\nUnigram Sentences: "
    for x in range(0,3):
        generateSentence(unigrams, masterList[0])
    print ""

    #bigrams
    calcMultigramCumulative(bigrams)
    print "\nBigram Sentences: "
    for x in range(0,3):
        generateBigramSentence(bigrams)
    print ""

    #trigrams
    calcMultigramCumulative(trigrams)
    print "\nTrigram Sentences: (will take a second)"
    count = 0
    while(count < 3):
        count += generateTrigramSentence(trigrams)
    print ""

    #quadgrams
    calcMultigramCumulative(quadgrams)
    print "\nQuadgram Sentences: (will take a second)"
    count = 0
    while(count < 3):
        count += generateQuadgramSentence(quadgrams)
    print ""


main()