import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

with open('text1.txt', 'r') as f:
    text = f.read()

# tokens = word_tokenize(text)

BAD_CHARS = ".!?,\'\"()"

tokens = [ word.lower().strip(BAD_CHARS) for word in text.strip().split() if len(word) > 4 ]

# Remove stop words
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

# Get the frequency distribution of the remaining tokens
freq_dist = nltk.FreqDist(filtered_tokens)

# Get the top 3 most frequent words as keywords
keywords = [pair[0] for pair in freq_dist.most_common(3)]
print(keywords)