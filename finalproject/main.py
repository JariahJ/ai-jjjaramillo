import nltk
nltk.download('punkt')
from nltk.stem.lancaster import LancasterStemmer

stemmer = LancasterStemmer()

import numpy as np
import tensorflow as tf
import random

import json
with open('intents.json') as json_data:
	intents = json.load(json_data)


# organization using natural language processor 
words = []
classes = []
documents = []
words_to_ignore = ['?']

for intent in intents['intents']:
    for pattern in intent['patterns']:
        list_of_words = nltk.word_tokenize(pattern)
        words.extend(list_of_words)
        documents.append((list_of_words, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

words = [stemmer.stem(w.lower()) for w in words if w not in words_to_ignore]

words = sorted(list(set(words)))

classes = sorted(list(set(classes)))

print(len(documents), "documents")
print(len(classes), "classes", classes)
print(len(words), "unique stemmed words", words)


