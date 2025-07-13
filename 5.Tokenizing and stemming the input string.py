import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer, WordNetLemmatizer
input_string = """
Amazon DynamoDB is a fully managed, serverless, key-value and document database designed to run high-performance applications at any scale.
"""

tokens = word_tokenize(input_string)
pstemmer = PorterStemmer()
lstemmer = LancasterStemmer()
sstemmer = SnowballStemmer("english")
lem = WordNetLemmatizer()
stemmed_words = [pstemmer.stem(word) for word in tokens]
stemmed_words1 = [lstemmer.stem(word) for word in tokens]
stemmed_words2 = [sstemmer.stem(word) for word in tokens]
lem_word = [lem.lemmatize(word) for word in tokens]
print(stemmed_words)
print(stemmed_words1)
print(stemmed_words2)
print(lem_word)
