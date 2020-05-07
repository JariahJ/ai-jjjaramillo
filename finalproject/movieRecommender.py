import nltk
nltk.download('punkt')
from nltk.stem.lancaster import LancasterStemmer

stemmer = LancasterStemmer()

import numpy as np
import tensorflow as tf
from tensorflow import keras
import random


import json
with open('movies.json') as json_data:
	intents = json.load(json_data)


# organization using natural language processor 
words = []
classes = []
documents = []
words_to_ignore = ['?']

for intent in intents['testData']:
    for pattern in intent['questions']:
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

#conver to numpy arrays
x_train = np.array(training_x)
y_train = np.array(training_y)


model = keras.Sequential()
model.add(keras.layers.Dense(9, input_dim=3359,  activation = 'relu')) #44
model.add(keras.layers.Dense(5, activation = 'softmax')) #9

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(x_train, y_train, epochs = 30, batch_size = 8)


#for users sentence they input
def clean_input(input):
        words_of_sentence = nltk.word_tokenize(input)
        words_of_sentence = [stemmer.stem(word.lower()) for word in words_of_sentence]
        return words_of_sentence
    
def collection_of_words(input, words, show_details=False):
    words_of_sentence = clean_input(input)
    collection = [0]*len(words)
    for s in words_of_sentence:
        for i,w in enumerate(words):
            if w==s:
                collection[i] = 1
                if show_details:
                    print("found in collection: %s" % w )
    return(np.array([collection]))

test = collection_of_words("what drama do you recommend?", words)

#########################################################

ERROR = 0.25
def classify(sentence):
        x = collection_of_words(sentence, words)
        answer = model.predict([x])[0]
        answer = [[i, r] for i,r in enumerate(answer) if r>ERROR]
        
        answer.sort(key=lambda x: x[1], reverse=True)
        return_list = []
        for a in answer:
            return_list.append((classes[a[0]], a[1]))
        return return_list
    
def response(sentence, user='123', show_details=False):
    answer = classify(sentence)
    if answer:
        while answer:
            for i in intents['testData']:
                if i['tag'] == answer[0][0]:
                    #selects a resonse from the intent
                    return print(random.choice(i['responses']))
            results.pop(0)

movie_title = "hi"
while movie_title != "exit":
	movie_title = input("Enter a movie title ")
	response(movie_title)
