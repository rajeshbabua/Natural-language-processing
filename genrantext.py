####You can Generate random text from the given text. 
def m(cfdist, word, num=20):
  for i in range(num):
    print(word, end=' ')
    word = cfdist[word].max()


text = "<s> Hurricane Hazel was the deadliest and costliest hurricane of the 1954 Atlantic hurricane season. The storm was named by the US Weather Bureau on October 5. In Haiti, 40% of the coffee trees and 50% of the cacao crop were lost, and at least 400 people were killed. Hazel struck North Carolina near Calabash on October 15 as a Category 4 hurricane. It destroyed most of the waterfront dwellings near its point of impact, including about 80% of those in Myrtle Beach, South Carolina. Heading north along the Atlantic coast of the United States, it caused $281 million in damage and 95 fatalities. Hazel struck Canada as an extratropical storm, raising the death toll by 81 people. Its effects were unprecedented in and around Toronto, due to a combination of heavy rainfall during the preceding weeks, the storm's unexpected retention of power and a lack of experience in dealing with tropical storms. Rivers and streams overflowed, causing over C$135 million of damage. <s>"
w= word_tokenize(text.lower())
len(w)
bi = nltk.bigrams(w)###########creates bi grams
tri= nltk.trigrams(w)######### trigrams
list(w)
cfd = nltk.ConditionalFreqDist(bi)#########conditional probability for bigrams
####note CondtionalFreqDist only works for bigrams i.e pairs 
#len(list(set(w))), len(w)

cfd['the']
m(cfd, 'hazel')########calling function and giving the word hazel to consider it as starting and create text
