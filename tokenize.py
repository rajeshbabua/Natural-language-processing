import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
text = "This tutorial is meant for those who want to get to know the Flow of TensorFlow. Ideally, you already know some of the Tensor of TensorFlow."
s_w = set(stopwords.words("english")
sents = sent_tokenize(text)
f_s = []
for w in words:
    if w not in s_w:
         f_s.append(w)
print (s_w)                   
print ("sents")
print(f_s)
