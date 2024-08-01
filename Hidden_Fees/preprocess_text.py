import nltk
import string
import spacy
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer

with open("/Users/kennethfrisardiii/Downloads/ForUsAll/Hidden_Fees/notes.txt") as f:
    texts = f.readlines()

text = ''
for i in range(len(texts)):
    text = text + texts[i]

words = word_tokenize(text)
sentences = sent_tokenize(text)
text = text.lower()
text = ' '.join(text.split())