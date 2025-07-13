from nltk.tag import RegexpTagger
from nltk.tokenize import word_tokenize

# Input text
text = "I spent $50 on January 1, 2023."

# Tokenize text
tokens = word_tokenize(text)

# Define regex patterns
patterns = [
    (r'\$\d+(\.\d{1,2})?', 'MONEY'),
    (r'\b\d{1,2}\/\d{1,2}\/\d{2,4}\b', 'DATE'),
    (r'\b(January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}, \d{4}\b', 'DATE'),
    (r'\d{4}', 'DATE'),
]

regex_tagger = RegexpTagger(patterns)
tagged_tokens = regex_tagger.tag(tokens)
print("Tagged Tokens:", tagged_tokens)
