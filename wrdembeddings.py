import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import gensim
from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from matplotlib import pyplot
sent1 = [['this', 'is', 'the', 'first', 'sentence', 'for', 'word2vec'],
            ['this', 'is', 'the', 'second', 'sentence'],
            ['yet', 'another', 'sentence'],
            ['one', 'more', 'sentence'],
            ['and', 'the', 'final', 'sentence']]
# train model
#sent1 = word_tokenize(sent)
#sent1

######## train model

model = Word2Vec(sent1,min_count =1)
model
##########summary of model

print(model)



#########summary of vocab
words = list(model.wv.vocab)
print (words)
r = model[model.wv.vocab]

###access vector for a word
print(model["sentence"])

######using principal component analysis
pca = PCA(n_components=2)
res= pca.fit_transform(r)

pyplot.scatter(res[:,0], res[:,1])

for i, word in enumerate(words):
    pyplot.annotate(word, xy=(res[i, 0], res[i, 1]))
pyplot.show()
