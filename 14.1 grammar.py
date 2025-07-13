import nltk
from nltk.parse.generate import generate
grammar = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> "Alice" | "Bob"
    VP -> "eats" "an apple" | "drinks" "water"
""")

# Generate sentences
for sentence in generate(grammar, n=10):
    print(" ".join(sentence))
