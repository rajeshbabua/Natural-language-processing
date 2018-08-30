import nltk
import numpy 
import sys
import matplotlib.pyplot as plt
from nltk.book import*
#text1.concordance("is")
#text1.similar("very")
#text1.common_context(["very","random"])
#print(len(text3))
#len(set(text3))
#len(set(text3))/len(text3)
#(text4.count("smote")
#(text4.count("lol")/len(text4))*100

def ld(text):
     return len(set(text))/len(text)

def pe(text):
     return 100*len(set(text))/len(text)
  
#print(pe (text3))
#print (ld (text3))
#print(len(set(text3)))
#print(len(sorted(text3)))
#type(ld)
sent1 =['call','ca','idh','.',"call"]
#ld(sent1)  
#sent1 + sent2  
#sent1.append("ghfr")
#sent1
#sent1[:3]
f = FreqDist(text1)
#f.most_common(50)
#f["the"]
#f.plot(50, cumulative=True)
#f.hapaxes()
v= set(text1)
lw = [w for w in v if len(w) >15 and f[w] >7 ]
len(set(lw))  
l = bigrams(text1)
#list(l)
#text1.collocations()
[len(w) for w in text1]
#f.plot()
len(set(word.lower() for word in v if word.isalpha()))
