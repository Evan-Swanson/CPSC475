"""
Team Member 1: Evan Swanson
Team Member 2: N/A 
GU Username of project lead: eswanson2
Project 7a:  This program generates a random sentence using unigrams, 
            bigrams, trigrams, and quadgrams based off of Shakespeare's
            entire collection of work
Due: 11/2/2018
"""
import re
import random
import pickle

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
    

    return [dictionary, count]
    

# *Way 2* (probability mass distributed over conditioning word)
# The top level dictionary holds the conditioning words as it's keys (the first word in the pair)
# Then, each key's value is a list with another dictionary and a counter variable
# Within each of those dictionaries are the various 2nd words in the bigrams that start
# with the conditioning word.  Those keys hold the individual and cumulative probabilities
# of that 2nd word given the conditioning word.







def makeBigrams(new):
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
            #check if first word is in the top dictionary
            if word in dictionary:
                #check if second word exists in dictionary of first word
                if nextWord in dictionary[word][0]:
                    # if yes, increase it's count as well as the total count for
                    # the first word
                    dictionary[word][0][nextWord][0] += 1
                    dictionary[word][1] += 1
                #else, make new entry in dictionary of first word that is the second word
                else:
                    dictionary[word][0][nextWord] = [1, 0]
                    dictionary[word][1] += 1
            #else create new entry for starting word
            else:
               #create list with dictionary for second words and counter variable
               dictionary[word] = [{}, 1]
               dictionary[word][0][nextWord] = [1, 0]

    #calculate each word's relative probability
    for x in dictionary:
        for y in dictionary[x][0]:
            #for each sub word (second in the par), take its count and divid by 
            # the count of the top level word (first in the pair)
            dictionary[x][0][y][0] = float(dictionary[x][0][y][0]) / float(dictionary[x][1])


    return dictionary

# same approach as the bigrams except the top level dictionary holds a 2 word pair
# instead of a single word, thus the new word is conditioned on the previous 2
def makeTrigrams(new):
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



    return dictionary

    
def makeQuadgrams(new):
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


    return dictionary



def main():
    fin = open("shakespeare.txt", 'r')
    string = fin.read()
    fin.close()
    string = re.sub(r'[.;:_!,?")(-]', ' ', string)
    string = re.sub(r'[\[\]]', ' ', string)
    string = re.sub('\n', ' </s> <s>  ', string)
    new = string.split()
    new = [x.lower() for x in new] #convert all to lowercase

    masterList = list()

    masterList.append(makeUnigrams(new)[1])
    masterList.append(makeUnigrams(new)[0])
    masterList.append(makeBigrams(new))
    masterList.append(makeTrigrams(new))
    masterList.append(makeQuadgrams(new))

    fout = open('proj7.pkl','wb')
    pickle.dump(masterList,fout)
    fout.close()


main()