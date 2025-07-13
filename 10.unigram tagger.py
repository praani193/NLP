import nltk
from nltk.corpus import treebank
from nltk.tag import UnigramTagger
from nltk.tag.brill import BrillTaggerTrainer, Template
from nltk.tag.brill_trainer import Pos

nltk.download('treebank')

train_sents = treebank.tagged_sents()[:3000]
test_sents = treebank.tagged_sents()[3000:]

unigram_tagger = UnigramTagger(train_sents)

templates = [
    Template(Pos([-1])),
    Template(Pos([1])),
    Template(Pos([-1, 0])),
    Template(Pos([0, 1])),
    Template(Pos([-2, -1])),
    Template(Pos([1, 2]))
]

brill_trainer = BrillTaggerTrainer(initial_tagger=unigram_tagger, templates=templates)
brill_tagger = brill_trainer.train(train_sents, max_rules=50)

accuracy = brill_tagger.evaluate(test_sents)
print("Brill Tagger Accuracy:", accuracy)

sentence = "The quick brown fox jumps over the lazy dog".split()
tagged_sentence = brill_tagger.tag(sentence)
print("Tagged Sentence:", tagged_sentence)
