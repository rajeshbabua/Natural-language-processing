import nltk
from nltk.tokenize import word_tokenize, sent_tokenize 
text= input("enter a sentence. you will it part of speech for each word")
t = nltk.word_tokenize(text)
for r in t:
  x = nltk.pos_tag(t)
print (x)
