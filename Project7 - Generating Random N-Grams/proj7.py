"""
Team Member 1: Evan Swanson
Team Member 2: N/A 
GU Username of project lead: eswanson2
Project 7:  This program generates a random sentence using unigrams, 
            bigrams, trigrams, and quadgrams based off of Shakespeare's
            entire collection of work
Due: 11/2/2018
"""
import re
import random
import pickle

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

def generateBigramSentence(dictionary, userOption):
    sentence = ""
    nextWord = "<s>"    #must start with beginning sentence marker
    
    for x in range(0, 12):
        numWords = dictionary[nextWord][1]
        index = float(random.randint(0, numWords)) / float(numWords)
        for z in dictionary[nextWord][0]:
            if dictionary[nextWord][0][z][1] > index and z != "</s>":
                currentWord = nextWord
                nextWord = z     
                sentence += " "+ currentWord
                break 
    if userOption == 'Y':
        sentence = sentence[5:].capitalize()
        sentence = "<s> " + sentence
        sentence = sentence + " </s>."
    else:
        sentence = sentence[5:].capitalize()
        sentence = sentence + "."
    print sentence

def generateTrigramSentence(dictionary, userOption):
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
    if userOption == 'Y':
        sentence = sentence[5:].capitalize()
        sentence = "<s> " + sentence
        sentence = sentence + " </s>."
        #if the sentence reached an end sentence marker with no other 
        # options before reaching 12 words, throw it out
        if len(sentence.split()) > 13:
            print sentence
            return 1
        else:
            return 0
    else:
        sentence = sentence[5:].capitalize()
        sentence = sentence + "."
        if len(sentence.split()) > 11:
            print sentence
            return 1
        else:
            return 0



def generateQuadgramSentence(dictionary, userOption):
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
    if userOption == 'Y':
        sentence = sentence[5:].capitalize()
        sentence = "<s> " + sentence
        sentence = sentence + " </s>."
        #if the sentence reached an end sentence marker with no other 
        #options before reaching 9 words, throw it out
        if len(sentence.split()) > 11:
            print sentence
            return 1
        else:
            return 0
    else:
        sentence = sentence[5:].capitalize()
        sentence = sentence + "."
        if len(sentence.split()) > 9:
            print sentence
            return 1
        else:
            return 0
    

def makeUnigrams(new):
    dictionary = {}
    count = 0

    #count each word's occurance
    for word in new:
        if word != '<s>' and word != '</s>':
            if word in dictionary:
                dictionary[word][0] += 1
                count += 1
            else:
                dictionary[word] = [1,0]
                count += 1

    #calculate each word's relative probability
    for x in dictionary:
        dictionary[x][0] = float(dictionary[x][0]) / float(count)
    
    cumulative = float(0)

    #calculate the cumulative probability
    for x in dictionary:
        cumulative = cumulative + dictionary[x][0]
        dictionary[x][1] = cumulative
    

    #generate 5 random sentences
    print "\nUnigram Sentences: "
    for x in range(0,3):
        generateSentence(dictionary, count)
    print ""

def makeBigrams(new, userOption):
    dictionary = {}
    count = 0

    #count each word's occurance
    for word in range(0,len(new)):
        length = len(new)
        if word != length - 1:
            #second word in pair
            nextWord = new[word + 1]
            #first word in pair
            word = new[word]
            #check if first word is in dictionary
            if word in dictionary:
                #check if second word exists in dictionary of first word
                if nextWord in dictionary[word][0]:
                    dictionary[word][0][nextWord][0] += 1
                    dictionary[word][1] += 1
                #make new pair
                else:
                    dictionary[word][0][nextWord] = [1, 0]
                    dictionary[word][1] += 1
            #create new entry for starting word
            else:
               #creat list with dictionary for second words and counter variable
               dictionary[word] = [{}, 1]
               dictionary[word][0][nextWord] = [1, 0]

    #calculate each word's relative probability
    for x in dictionary:
        for y in dictionary[x][0]:
            dictionary[x][0][y][0] = float(dictionary[x][0][y][0]) / float(dictionary[x][1])

    #calculate the cumulative probability
    for x in dictionary:
        cumulative = float(0)
        for y in dictionary[x][0]:
            cumulative += dictionary[x][0][y][0]
            dictionary[x][0][y][1] = cumulative

    #generate 3 random sentences
    print "\nBigram Sentences: "
    for x in range(0,3):
        generateBigramSentence(dictionary, userOption)
    print ""

def makeTrigrams(new, userOption):
    dictionary = {}
    count = 0

    #count each word's occurance
    for word in range(0,len(new) - 2):
        length = len(new)
        nextWord = new[word + 2]
        word = new[word] + " " + new[word + 1]
        if word in dictionary:
            if nextWord in dictionary[word][0]:
                dictionary[word][0][nextWord][0] += 1
                dictionary[word][1] += 1
            else:
                dictionary[word][0][nextWord] = [1, 0]
                dictionary[word][1] += 1
        else:
           dictionary[word] = [{}, 1]
           dictionary[word][0][nextWord] = [1, 0]

    #calculate each word's relative probability
    for x in dictionary:
        for y in dictionary[x][0]:
            dictionary[x][0][y][0] = float(dictionary[x][0][y][0]) / float(dictionary[x][1])

    #calculate the cumulative probability
    for x in dictionary:
        cumulative = float(0)
        for y in dictionary[x][0]:
            cumulative += dictionary[x][0][y][0]
            dictionary[x][0][y][1] = cumulative

    #generate 3 random sentences
    print "\nTrigram Sentences: (will take a second)"
    while(count < 3):
        count += generateTrigramSentence(dictionary, userOption)
    print ""
    
def makeQuadgrams(new, userOption):
    dictionary = {}
    count = 0

    #count each word's occurance
    for word in range(0,len(new) - 3):
        nextWord = new[word + 3]
        word = new[word] + " " + new[word + 1] + " " + new[word + 2]
        if word in dictionary:
            if nextWord in dictionary[word][0]:
                dictionary[word][0][nextWord][0] += 1
                dictionary[word][1] += 1
            else:
                dictionary[word][0][nextWord] = [1, 0]
                dictionary[word][1] += 1
        else:
           dictionary[word] = [{}, 1]
           dictionary[word][0][nextWord] = [1, 0]

    #calculate each word's relative probability
    for x in dictionary:
        for y in dictionary[x][0]:
            dictionary[x][0][y][0] = float(dictionary[x][0][y][0]) / float(dictionary[x][1])

    #calculate the cumulative probability
    for x in dictionary:
        cumulative = float(0)
        for y in dictionary[x][0]:
            cumulative += dictionary[x][0][y][0]
            dictionary[x][0][y][1] = cumulative

    #generate 3 random sentences
    print "\nQuadgram Sentences: (will take a second)"
    while(count < 3):
        count += generateQuadgramSentence(dictionary, userOption)
    print ""

def deserialize():
    fin = open('proj7.pkl', 'rb')
    lsts_in = pickle.load(fin)
    fin.close()
    return lsts_in

def main():
    masterList = deserialize()

    print masterList[1]
    print masterList[0]

    print "\nUnigram Sentences: "
    for x in range(0,3):
        generateSentence(masterList[1], masterList[0])
    print ""

    print "\nBigram Sentences: "
    for x in range(0,3):
        generateBigramSentence(masterList[2])
    print ""


main()