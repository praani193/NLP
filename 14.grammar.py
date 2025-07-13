from nltk import CFG
from nltk.parse.generate import generate

grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N | Det N PP
    VP -> V NP | V NP PP
    PP -> P NP
    Det -> 'the' | 'a'
    N -> 'dog' | 'cat' | 'park'
    V -> 'saw' | 'chased'
    P -> 'in' | 'with'
""")

print("Generated Sentences:")
for sentence in generate(grammar, n=10):
    print(' '.join(sentence))


