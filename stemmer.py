import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
words = ["python", "pythonnning", "programme", "program" ]
ps = PorterStemmer()
for w in words:
  print (ps.stem(w))
