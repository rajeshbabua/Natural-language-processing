#########################################################################
#### Regular expressions
#########################################################################
import re
import nltk
from nltk import corpus
wd = [w for w in nltk.corpus.words.words('en') if w.islower()]
[w for w in wd if re.search('ed$',w)]
[w for w in wd if re.search('...j..t..$',w)]
[w for w in wd if re.search('^ad',w)]
[w for w in wd if re.search('^[abc][mno][jlk][def]$',w)]
[w for w in wd if re.search('[abc]',w)]
[w for w in wd if re.search('[a-z0-9]',w)]
[w for w in wd if re.search('<acu(s|ed|ing)ed>',w)]
[w for w in wd if re.search('e*',w)]
[w for w in wd if re.search('a+',w)]
[w for w in wd if re.search('ed?',w)]
[w for w in wd if re.search('a{2}',w)] ####### atleast 2 times
[w for w in wd if re.search('ad{2,}',w)]#### min 2 times.. max
[w for w in wd if re.search('ad{,2}$',w)]  ##### max 2 times
##########################################

word = 'supercalifragilisticexpialidocious'
re.findall(r'[aeiou]',word)
######## "r allows the interpreter to treat it as a raw string ratehr than a string"#######
########### more useful when dealing with backslashes

re.findall(r'^.*(ing|ly|ed|ious|ies|ive|es|s|ment)$', 'process')
