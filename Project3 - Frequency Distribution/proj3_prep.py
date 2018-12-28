def tokenize(string_in):
    import re
    string = re.sub('\n',' ', string_in)
     #create a list containing all lower case characters
    good_chars = [chr(value) for value in range(ord('a'),ord('z') + 1,1)]
    good_chars.append(' ')
    string = string.lower()
    new_str = ''
    for ch in string:
        if ch in good_chars:
            new_str = new_str + ch
    return new_str

def write_files():
    import nltk
    import re
    import pickle
    files = nltk.corpus.inaugural.fileids()
    from nltk.corpus import inaugural

    masterList = list()
    for i in files:
        sentences = inaugural.sents(i)
	sentLst = [' '.join(sent) + '\n' for sent in sentences]
        theString = str(sentLst)
        fixedString = tokenize(theString)
        masterList.append(fixedString)

    fout = open('proj3.pkl','wb')
    pickle.dump(masterList,fout)
    fout.close()


'''

def write_files(id):
    import nltk
    from nltk.corpus import inaugural
    sentences = inaugural.sents(id)
    
    sentLst = [' '.join(sent) + '\n' for sent in sentences]
    txt = ''.join(sentLst)
    id = id.split('.')  #eliminate the final 'txt' from some corpora
    filename = id[0] + '.txt' 
    outfile = open(filename, 'w') 
    outfile.write(txt)
    outfile.close()
'''

def main():
   write_files()
  
main()
