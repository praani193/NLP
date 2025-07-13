from nltk.tag import NgramTagger
from nltk.corpus import treebank
import nltk
train_sents = treebank.tagged_sents()[:3000]
test_sents = treebank.tagged_sents()[3000:]
ngram_tagger = NgramTagger(2, train=train_sents)
accuracy1 = ngram_tagger.accuracy(test_sents)

print("N-gram Tagger Accuracy:",accuracy1)