'''To be used for stemming words and expressions for WFConcordance'''
import sys
from nltk.stem import PorterStemmer
from nltk.stem.snowball import RussianStemmer
from nltk.stem.snowball import GermanStemmer


def stemWord(word, lng):
    '''Stems word based on lng and returns the stemmed version'''
    if lng == 'ru':
        stemmer = RussianStemmer()
    elif lng == 'en':
        stemmer = PorterStemmer()
    elif lng == 'de':
        stemmer = GermanStemmer()
    else:
        return "NA"

    word = word.lower() #otherwise the stemmer fails
    return stemmer.stem(word)

def stemForWf (expression, language):
    '''Processes the expr_lng_tuple and returns the stemmed expression/word'''
    return '+'.join([stemWord(word, language) for word in expression])


if __name__ == '__main__':
    output = stemForWf(sys.argv[1:-1], sys.argv[-1])
    print(output)
