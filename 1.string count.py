import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

paragraph = """
Amazon DynamoDB is a fully managed, serverless, key-value and document database designed to run high-performance applications at any scale. 
It automatically scales up and down to adjust for capacity and maintains low latency, with no need to manage servers or clusters. 
It is often used for applications that require high availability and seamless scalability, such as mobile apps and IoT.
"""

tokens = word_tokenize(paragraph.lower())
word_frequency = FreqDist(tokens)

print("Word Frequencies:")
for word, freq in word_frequency.items():
    print(f"{word}: {freq}")
