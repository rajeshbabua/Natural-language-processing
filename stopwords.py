import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
text = "This tutorial is meant for those who want to get to know the Flow of TensorFlow. Ideally, you already know some of the Tensor of TensorFlow."
# stopwords set limited to english language 
sw = set(stopwords.words("english"))
#print (sw)
# filtering the above sentence for stopwords
filter = [] 
# empty array
words = word_tokenize(text)
#print (words)
for word in words:
  if word not in sw:
    filter.append(words)
print (filter)
    
