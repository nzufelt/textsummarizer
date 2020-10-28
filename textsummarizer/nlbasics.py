import nltk
from pprint import pprint

# Tokenizing module
text = input ("Enter your text to tokenize here: ")
from nltk.tokenize import word_tokenize, sent_tokenize
# Stopwords module
from nltk.corpus import stopwords
from string import punctuation
# Bigrams module
from nltk.collocations import *
# Stemming module
from nltk.stem.lancaster import LancasterStemmer
# Disambiguation module
from nltk.corpus import wordnet as wn
from nltk.wsd import lesk

# Tokenizing text
def do_tokenize():
    text = input ("Enter your text to tokenize here: ")

    sents=sent_tokenize(text)
    print(sents)

    words=[word_tokenize(sent) for sent in sents]
    print(words)

# Removing stopwords
def do_removestopwords():
    text = input ("Enter your text here: ")

    customStopWords=set(stopwords.words('english')+list(punctuation))
    wordsWOStopwords=[word for word in word_tokenize(text) if word not in customStopWords]
    print(wordsWOStopwords)

#Identifying bigrams
def do_identifybigrams():
    text = input ("Enter your text here: ")

    customStopWords=set(stopwords.words('english')+list(punctuation))
    wordsWOStopwords=[word for word in word_tokenize(text) if word not in customStopWords]
    print(wordsWOStopwords)

    bigram_measures = nltk.collocations.BigramAssocMeasures()
    finder = BigramCollocationFinder.from_words(wordsWOStopwords)
    print(finder.ngram_fd.items())

# Stemming
def do_stemming():
    text = input ("Enter your text here: ")

    st = LancasterStemmer()
    stemmedWords = [st.stem(word) for word in word_tokenize(text)]
    print(stemmedWords)

# POS Tagging
def do_POStagging():
    text = input ("Enter your text here: ")

    tagList = nltk.pos_tag(word_tokenize(text))
    pprint(tagList)

# Disambiguating word meanings
def do_worddisambiguation():
    word = input ("Enter your word here: ")
    for ss in wn.synsets(word):
        print(ss, ss.definition())

    text2 = input ("Enter a sentence with that previous word: ")
    contextualsentence = lesk(word_tokenize(text2), word)
    print(contextualsentence, contextualsentence.definition())

menu = """
1: Tokenize text
2: Remove stopwords
3: Find bigrams
4: Word stemmer
5: Part of speech tagging
6: Word disambiguation (must enter single word)
"""

print(menu)
choice = input ("Input your choice [1]: " )

if choice == "2":
    do_removestopwords()
elif choice == "3":
    do_identifybigrams()
elif choice == "4":
    do_stemming()
elif choice == "5":
    do_POStagging()
elif choice == "6":
    do_worddisambiguation()
else:
    do_tokenize()
