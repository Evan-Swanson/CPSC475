import matplotlib.pyplot as plt
import pickle
import re


def deserialize():
    fin = open('proj3.pkl', 'rb')
    lsts_in = pickle.load(fin)
    fin.close()
    return lsts_in

def getUserWord():
    raw = raw_input("Enter a word: ")
    singleWord = " " + raw + " "
    return singleWord

def countWords(masterList, userWord):

   frequency = []
   for speech in masterList:
	matches = re.findall(userWord, speech)
	frequency.append(len(matches))
   return frequency
   

def main():
   masterList = deserialize()
   userWord = getUserWord()
   frequencyTable = countWords(masterList, userWord)
   years = [(i*4 + 1789) for i in range(56)]
   plt.plot(years,frequencyTable)
   title = 'Year vs. Frequency of "' + userWord + '"in Inaugural Addresses'
   plt.title(title)
   plt.xlabel("Year")
   plt.ylabel("Frequency")
   plt.show()


main()
