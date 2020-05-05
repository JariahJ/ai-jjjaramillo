import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy as np
import tflearn
import tensorflow as tf
import random

import json
with open('intents.json') as json_data:
	intents = json.load(json_data)


# organization using natural language processor 
words = []
classes = []
document = []
words_to_ignore = ['?']

for intent in intents['intents']:
	for pattern in intent['patterns']:
	list_of_words = nltk.word_tokenize(pattern)
	words.add(word)
	documents.append((list_of_words, intent['tag']))

	if intent['tag'] not in classes:
		classes.append(intent['tag'])


