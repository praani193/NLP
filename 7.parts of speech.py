from nltk import pos_tag
from nltk.tokenize import word_tokenize
import nltk
text = "Amazon DynamoDB is a fully managed database designed to run high-performance applications."
tokens = word_tokenize(text)
pos_tags = pos_tag(tokens)
print("Parts of Speech:",pos_tags)