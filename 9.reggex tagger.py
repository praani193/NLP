
from nltk.tag import RegexpTagger
from nltk.tokenize import word_tokenize
import nltk
text = "He is running fast and finished the race with flying colors."

tokens = word_tokenize(text)

patterns = [
    (r'.*ing$', 'VBG'),
    (r'.*ed$', 'VBD'),
    (r'.*es$', 'VBZ'),
    (r'.*ould$', 'MD'),
    (r'.*\'s$', 'POS'),
    (r'.*s$', 'NNS'),
    (r'^-?[0-9]+(\.[0-9]+)?$', 'CD'),
    (r'.*', 'NN')
]

regex_tagger = RegexpTagger(patterns)
regex_tagged = regex_tagger.tag(tokens)

print("Regex Tagger Output:", regex_tagged)