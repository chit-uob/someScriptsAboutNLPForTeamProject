import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer, WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

# Sample forum question
question = "Dear Sir, I have questions about the first individual submission. For kanban feature cards and personas, each member with the group should submit their own individualized version for them right?  So totally 7 personas and 7 kanban feature cards right?   And for mockup of functionality, you still need 7 different individualized versions of mockups yet under the same app development topic right? Thank you!"

# Define stopwords, stemmer, and lemmatizer
stop_words = set(stopwords.words('english'))
stemmer = SnowballStemmer('english')
lemmatizer = WordNetLemmatizer()

# Perform text preprocessing: remove stopwords, stem, and lemmatize
preprocessed_question = [lemmatizer.lemmatize(stemmer.stem(word))
                         for word in question.lower().split()
                         if word not in stop_words]

# Join the preprocessed question into a single string
preprocessed_question = ' '.join(preprocessed_question)

# Create a dataframe with the preprocessed question as a single row
df = pd.DataFrame({'question': [preprocessed_question]})

# Initialize TfidfVectorizer object
tfidf = TfidfVectorizer()

# Fit and transform the preprocessed question to obtain the TF-IDF matrix
tfidf_matrix = tfidf.fit_transform(df['question'])

# Get the feature names (i.e., the terms) from the TF-IDF matrix
feature_names = tfidf.get_feature_names_out()

# Get the TF-IDF scores for each term in the preprocessed question
tfidf_scores = tfidf_matrix.toarray()[0]

# Create a dictionary of the terms and their corresponding TF-IDF scores
terms_tfidf = dict(zip(feature_names, tfidf_scores))

# Get the top 3 terms with the highest TF-IDF scores
top_terms = sorted(terms_tfidf.items(), key=lambda x: x[1], reverse=True)[:3]

# Print the top terms as tags
tags = [term[0] for term in top_terms]
print("Tags:", tags)
