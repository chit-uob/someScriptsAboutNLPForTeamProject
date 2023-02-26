import nltk
import spacy
from spacy.tokens import Doc
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

with open('text1.txt', 'r') as f:
    text1 = f.read()

with open('text2.txt', 'r') as f:
    text2 = f.read()

BAD_CHARS = ".!?,\'\"()"

tokens1 = [ word.lower().strip(BAD_CHARS) for word in text1.strip().split() if len(word) > 4 ]
tokens2 = [ word.lower().strip(BAD_CHARS) for word in text2.strip().split() if len(word) > 4 ]

# Remove stop words
stop_words = set(stopwords.words('english'))
filtered_tokens1 = [word for word in tokens1 if word.lower() not in stop_words]
filtered_tokens2 = [word for word in tokens2 if word.lower() not in stop_words]

nlp = spacy.load("en_core_web_lg")

doc1 = nlp(Doc(nlp.vocab, words=filtered_tokens1))
doc2 = nlp(Doc(nlp.vocab, words=filtered_tokens2))

print(doc1.similarity(doc2), doc1, "<->", doc2)


## Get the frequency distribution of the remaining tokens
# freq_dist1 = nltk.FreqDist(filtered_tokens1)
# freq_dist2 = nltk.FreqDist(filtered_tokens2)
#
# # Get the top 3 most frequent words as keywords
# keywords = [pair[0] for pair in freq_dist.most_common(3)]
# print(keywords)