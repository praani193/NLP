from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import nltk


paragraph =  """
Amazon DynamoDB is a fully managed, serverless, key-value and document database designed to run high-performance applications at any scale. 
It automatically scales up and down to adjust for capacity and maintains low latency, with no need to manage servers or clusters. 
It is often used for applications that require high availability and seamless scalability, such as mobile apps and IoT.
"""

stop_words = set(stopwords.words('english'))
tokens = word_tokenize(paragraph.lower())
word_frequency = FreqDist(tokens)

filtered_tokens = [word for word in tokens if word.isalpha() and word not in stop_words and word_frequency[word] > 1]
print("Filtered Tokens:", filtered_tokens)
