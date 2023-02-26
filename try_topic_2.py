import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from gensim.utils import simple_preprocess

def extract_topics(text):
    # Tokenize the text into sentences and words
    sentences = sent_tokenize(text)
    words = simple_preprocess(text)

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.lower() not in stop_words]

    # Lemmatize the words
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]

    # Identify the most common words
    freq_dist = nltk.FreqDist(words)
    common_words = freq_dist.most_common(10)

    # Extract topics from the common words
    topics = [word[0] for word in common_words]

    return topics

with open('text1.txt', 'r') as f:
    text = f.read()

topics = extract_topics(text)
print(topics)