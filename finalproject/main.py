import nltk
nltk.download('punkt')
from nltk.stem.lancaster import LancasterStemmer

stemmer = LancasterStemmer()

import numpy as np
import tensorflow as tf
from tensorflow import keras
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

training = []
output = []

output_empty = [0] * len(classes)

for document in documents:
    bag = []
    pattern_words = document[0]
    pattern_words = [stemmer.stem(word.lower()) for word in pattern_words]

    for i in range(len(words)):
        if words[i] in pattern_words:
            bag.append(1)
        else:
            bag.append(0)

    output_row = list(output_empty)
    output_row[classes.index(document[1])] = 1

    training.append([bag, output_row])

random.shuffle(training)
training = np.array(training)

training_x = list(training[:,0])
training_y = list(training[:,1])

x_train = np.array(training_x)
y_train = np.array(training_y)


model = keras.Sequential()
model.add(keras.layers.Dense(9, input_dim=44,  activation = 'relu'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(x_train, y_train, epochs = 10)

