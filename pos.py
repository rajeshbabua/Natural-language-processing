import nltk
from nltk.tokenize import word_tokenize, sent_tokenize 
text="""the time of the dayb isver good and i dont not how itwas a wonmderful opportunity 
so uimeantitajdfuj the way i w"""
t = nltk.word_tokenize(text)
for r in t:
  x = nltk.pos_tag(t)
print (x)
