#########################################################################
#### Regular expressions
#########################################################################
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
wds = [w for w in nltk.corpus.words.words('en') if w.islower()]
[w for w in wds if re.search('a$',w)]
[w for w in wds if re.search('...d...t..^',w)]
[w for w in wds if re.search('d^',w)] 
