import nltk
from nltk.classify import MaxentClassifier
train_data = [
    ({"word": "good"}, "positive"),
    ({"word": "bad"}, "negative"),
    ({"word": "excellent"}, "positive"),
    ({"word": "terrible"}, "negative"),
]
classifier = MaxentClassifier.train(train_data, max_iter=10)
test_data = {"word": "good"}
print(classifier.classify(test_data))
classifier.show_most_informative_features(5)
