'''
Another attempt to code a term base
'''

import codecs
import os
import termEntryClass
from nltk.stem import PorterStemmer
from nltk.stem.snowball import RussianStemmer
from nltk.stem.snowball import GermanStemmer


class termBase(object):
    def __init__(self, filename, encoding):
        self.fileName = filename
        self.encoding = encoding
        if not os.path.exists(filename):
            codecs.open(filename, 'w', encoding).close()

    def __readFile(self):
        f = codecs.open(self.fileName, 'r', self.encoding)
        text = f.readlines()
        f.close()
        data = []
        for line in text:
            elems = line.strip().split('\t')
            if len(elems) == 2:
                entry = termEntryClass.termEntry(elems[0], elems[1])
            elif len(elems) == 3:
                entry = termEntryClass.termEntry(elems[0], elems[1], elems[2])
            else:
                continue
            data.append(entry)
        return data

    def __writeFile(self, data):
        f = codecs.open(self.fileName, 'w', self.encoding)
        for i in data:
            f.write(str(i))
        f.close()

    def readTerms(self):
        data = self.__readFile()
        return data

    def writeTerms(self, data):
        self.__writeFile(data)

    def writeTerm(self, src, trg, comment):
        pass

    def delTerm(self, src):
        pass

    def sortTerms(self):
        pass

    def findTerm(self, src):
        pass

    def displayTerms(self, src):
        pass

    def stemWord(self, word, lng):
        '''Separates the word's changeable part with a '|' for wordfast'''
        if lng == 'ru':
            stemmer = RussianStemmer()
        elif lng == 'en':
            stemmer = PorterStemmer()
        elif lng == 'de':
            stemmer = GermanStemmer()
        else:
            print('Language error. Exiting...')
            sys.exit(1)

        word = word.lower() #otherwise the stemmer fails
        if len(word) <= 3:
            return word
        elif len(word) == len(stemmer.stem(word)):
            return "{0}|{1}".format(word[:-1], word[-1])
        else:
            return "{0}|{1}".format(word[:len(stemmer.stem(word))], \
            word[len(stemmer.stem(word)):])

    def stemTerms (self, language):
        '''Processes the term list and returns a list with generalized terms'''
        data = self.readTerms()
        for entry in data:
            words = entry.src_term.split()
            entry.src_term = ' '.join([self.stemWord(word, language) for word in words])
        self.writeTerms(data)

    def unstemTerms(self):
        data = self.readTerms()
        for entry in data:
            entry.src_term = entry.src_term.replace('|', '')
        self.writeTerms(data)

    def main():
        pass

if __name__ == '__main__':
    main()




