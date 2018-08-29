import nltk
# nltk.download()-----> use  this to downlaod all packages required for nltk 
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
text = "This tutorial is meant for those who want to get to know the Flow of TensorFlow. Ideally, you already know some of the Tensor of TensorFlow."
sents = sent_tokenize(text)
print ("sents")
words = word_tokenize(text)
print ("words")
