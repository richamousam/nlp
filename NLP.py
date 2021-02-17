#Data set of Italian recipes from https://www.gutenberg.org/ebooks/24407 (public domain)
#The txt format of this has been split into multiple files, one recipe per file.
#There are 220 recipes

#Load the data
#Firstly, we load all the data into the documents dictionary
#We also merge the documents into one big string, corpus_all_in_one, for convenience





import os
data_folder = os.path.join('recipes')
all_recipe_files = [os.path.join(data_folder, fname)
                    for fname in os.listdir(data_folder)]
documents = {}
for recipe_fname in all_recipe_files:
    bname = os.path.basename(recipe_fname)
    recipe_number = os.path.splitext(bname)[0]
    with open(recipe_fname, 'r') as f:
        documents[recipe_number] = f.read()

corpus_all_in_one = ' '.join([doc for doc in documents.values()])

print("Number of docs: {}".format(len(documents)))
print("Corpus size (char): {}".format(len(corpus_all_in_one)))

#Tokenisation is the process of splitting a raw string into a list of tokens
from nltk.tokenize import word_tokenize

try:  # py3
    all_tokens = [t for t in word_tokenize(corpus_all_in_one)]
except UnicodeDecodeError:  # py27
    all_tokens = [t for t in word_tokenize(corpus_all_in_one.decode('utf-8'))]

print("Total number of tokens: {}".format(len(all_tokens)))


#Counting Words
#We start with a simple word count using collections.Counter

#We are interested in finding:
#(1) how many times a word occurs across the whole corpus (total number of occurrences)
#(2) in how many documents a word occurs

from collections import Counter

total_term_frequency = Counter(all_tokens)

for word, freq in total_term_frequency.most_common(20):
    print("{}\t{}".format(word, freq))
    
    
    document_frequency = Counter()

for recipe_number, content in documents.items():
    tokens = word_tokenize(content)
    unique_tokens = set(tokens)
    document_frequency.update(unique_tokens)

for word, freq in document_frequency.most_common(20):
    print("{}\t{}".format(word, freq))
    
    
    #Stop-words
from nltk.corpus import stopwords
import string

print(stopwords.words('english'))
print(len(stopwords.words('english')))
print(string.punctuation)


stop_list = stopwords.words('english') + list(string.punctuation)
tokens_no_stop = [token for token in all_tokens
                        if token not in stop_list]
total_term_frequency_no_stop = Counter(tokens_no_stop)
for word, freq in total_term_frequency_no_stop.most_common(20):
    print("{}\t{}".format(word, freq))
    
    #Notice When and The above (uppercase W and T)
#Different variations of the same words are counted as different words (they are, after all, different strings)


print(total_term_frequency_no_stop['olive'])
print(total_term_frequency_no_stop['olives'])
print(total_term_frequency_no_stop['Olive'])
print(total_term_frequency_no_stop['Olives'])
print(total_term_frequency_no_stop['OLIVE'])
print(total_term_frequency_no_stop['OLIVES'])


#Text Normalisation using Stemming
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
all_tokens_lower = [t.lower() for t in all_tokens]
tokens_normalised = [stemmer.stem(t) for t in all_tokens_lower
                                     if t not in stop_list]
total_term_frequency_normalised = Counter(tokens_normalised)
for word, freq in total_term_frequency_normalised.most_common(20):
    print("{}\t{}".format(word, freq))
    
    
    #Getting ngrams
from nltk import ngrams

phrases = Counter(ngrams(all_tokens_lower, 2))
for phrase, freq in phrases.most_common(20):
    print("{}\t{}".format(phrase, freq))
    
    
    phrases = Counter(ngrams(all_tokens_lower, 3))
for phrase, freq in phrases.most_common(20):
    print("{}\t{}".format(phrase, freq))
    
    
    #n-grams and stop-words
#Stop-word removal will affect n-grams
phrases = Counter(ngrams(tokens_no_stop, 2))

for phrase, freq in phrases.most_common(20):
    print("{}\t{}".format(phrase, freq))
    
    
    phrases = Counter(ngrams(tokens_no_stop, 3))

for phrase, freq in phrases.most_common(20):
    print("{}\t{}".format(phrase, freq))
