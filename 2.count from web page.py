import nltk
from nltk.tokenize import word_tokenize
import requests
from bs4 import BeautifulSoup

url = "https://www.google.com"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
url_text = soup.get_text()

tokens = word_tokenize(url_text.lower())
numbers = [token for token in tokens if token.isdigit()]
words = [token for token in tokens if token.isalpha()]
expressions = [token for token in tokens if not token.isalnum()]

print("Numbers:", numbers)
print("Words:", words)
print("Expressions:", expressions)
