import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
words = ["python", "pythonnning", "programme", "program" ]
for w in words:
  print (PorterStemmer.stem(w))
