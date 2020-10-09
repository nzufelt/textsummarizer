import nltk

text="Mary had a little lamb. Her fleece was white as snow"
from nltk.tokenize import word_tokenize, sent_tokenize

sents=sent_tokenize(text)
print(sents)

words=[word_tokenize(sent) for sent in sents]
print(words)

from nltk.corpus import stopwords
from string import punctuation
customStopWords=set(stopwords.words('english')+list(punctuation))
wordsWOStopwords=[word for word in word_tokenize(text) if word not in customStopWords]
print(wordsWOStopwords)

