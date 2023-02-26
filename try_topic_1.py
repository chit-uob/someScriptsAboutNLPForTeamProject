import gensim
from gensim.utils import simple_preprocess
from gensim.models import LdaModel
from gensim.corpora import Dictionary
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords


def extract_topics(text):
    # Tokenize the text into words
    words = list(simple_preprocess(text))

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.lower() not in stop_words]

    # Lemmatize the words
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]

    # Create a dictionary from the words
    dictionary = Dictionary([words])

    # Create a bag-of-words representation of the text
    corpus = [dictionary.doc2bow(words)]

    # Build an LDA model with one topic
    lda_model = LdaModel(corpus=corpus, num_topics=1, id2word=dictionary)

    # Extract the topic from the model
    topic = lda_model.show_topics(num_words=10)[0][1]
    topic = topic.split("+")
    topic = [t.strip().split("*")[1].replace('"', '') for t in topic]

    return topic

with open('text1.txt', 'r') as f:
    text = f.read()

topics = extract_topics(text)
print(topics)