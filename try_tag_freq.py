text = """

I am curious if there is an algorithm/method exists to generate keywords/tags from a given text, by using some weight calculations, occurrence ratio or other tools.

Additionally, I will be grateful if you point any Python based solution / library for this.

Thanks

"""
BAD_CHARS = ".!?,\'\"()"

# transform text into a list words--removing punctuation and filtering small words
words = [ word.lower().strip(BAD_CHARS) for word in text.strip().split() if len(word) > 4 ]

word_freq = {}

# generate a 'word histogram' for the text--ie, a list of the frequencies of each word
for word in words :
  word_freq[word] = word_freq.get(word, 0) + 1

# sort the word list by frequency
# (just a DSU sort, there's a python built-in for this, but i can't remember it)
tx = [ (v, k) for (k, v) in word_freq.items()]
tx.sort(reverse=True)
word_freq_sorted = [ (k, v) for (v, k) in tx ]

# eg, what are the most common words in that text?
print(word_freq_sorted)
# returns: [('which', 4), ('other', 4), ('like', 4), ('what', 3), ('upon', 3)]
# obviously using a text larger than 50 or so words will give you more meaningful results

term_importance = lambda word : 1.0/word_freq[word]

# select document keywords from the words at/near the top of this list:
map(term_importance, word_freq.keys())