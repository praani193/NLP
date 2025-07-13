import nltk
from nltk.probability import FreqDist
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

url = "https://www.google.com"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
text = soup.get_text()

tokens = nltk.word_tokenize(text.lower())
words = [token for token in tokens if token.isalpha()]
freq_dist = FreqDist(words)
print("Word Frequencies:")
for word, freq in freq_dist.items():
    print(f"{word}: {freq}")
freq_dist.plot(30, cumulative=False)
plt.show()
