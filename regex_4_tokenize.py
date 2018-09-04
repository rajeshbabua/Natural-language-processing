######## nltk regular expression tokenizer######
import nltk
import re
from nltk.tokenize import regexp_tokenize
text = """'For now, you don't need to understand the difference between the notations f(w) and w.f(). Instead, simply learn this Python idiom which performs the same 
 ...operation on every element of a list. In the preceding examples, it goes through each word in text1, assigning each one in turn to the variable w and performing the specified operation on the variable."""
pattern = r'''(?x)   ####set flag to allow verbose regexps 
...       ([A-Z]\.)+  ### abbrevations,  e.g U.S.A
...       | \w+(-\w+)*  ## words with optional internal hyphens
...       | \$?\d(\.\d+)?%?  ##currency with percentages, e.g $12.40, 82%
...       | \.\.\.     ## ellipsis
...       |[][.,;"'?():-_`]  ##there are separate tokens; includes ], [
...'''
nltk.regexp_tokenize(text,pattern)
