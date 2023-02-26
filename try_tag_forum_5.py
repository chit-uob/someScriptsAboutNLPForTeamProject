import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

# Example forum post
post = "I wanted to constantly check for internet connection status in order to block my Application (with a dialog window informing the issue) until the network is re-established. Since I'm not using Compose for Android, I don't have access to ConnectivityManager class as I've seen been used in other related answers to this question online. How can I achieve this in Compose for Desktop?"

# Tokenize the text
tokens = word_tokenize(post)

# Remove stop words
stop_words = set(stopwords.words('english'))
filtered_tokens = [word.lower() for word in tokens if word.lower() not in stop_words]

# Stem the words
stemmer = nltk.PorterStemmer()
stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]

# Count word frequency
word_freq = Counter(stemmed_tokens)

# Get the top 3 keywords
keywords = [pair[0] for pair in word_freq.most_common(3)]
print(keywords)