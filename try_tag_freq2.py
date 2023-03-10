import nltk
from nltk.collocations import *
bigram_measures = nltk.collocations.BigramAssocMeasures()

# change this to read in your data
# finder = BigramCollocationFinder.from_words(
#    nltk.corpus.genesis.words('english-web.txt'))
finder = BigramCollocationFinder.from_words(
    nltk.corpus.genesis.words('english-web.txt'))

# only bigrams that appear 3+ times
finder.apply_freq_filter(3)

# return the 5 n-grams with the highest PMI
results = finder.nbest(bigram_measures.pmi, 5)
print(results)