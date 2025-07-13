from nltk.classify import MaxentClassifier
from nltk.corpus import movie_reviews
import nltk
def extract_features(words):
    return {word: True for word in words}

documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

train_data = [(extract_features(words), category) for words, category in documents[:1500]]
test_data = [(extract_features(words), category) for words, category in documents[1500:2000]]

classifier = MaxentClassifier.train(train_data, max_iter=10)

accuracy = nltk.classify.accuracy(classifier, test_data)
print("Maximum Entropy Classifier Accuracy:", accuracy)
