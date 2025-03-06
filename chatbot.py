import random
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
import tensorflow as tf

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Load intents
with open(r'C:\Users\Nandani\OneDrive\Desktop\mini project\intents.json') as file:
    intents = json.load(file)

# Initialize words, classes, and documents lists
words = []
classes = []
documents = []
ignoreLetters = ['?', '!', '.', ',']

# Tokenize and process each pattern in the intents file
for intent in intents['intents']:
    for pattern in intent['patterns']:
        wordList = nltk.word_tokenize(pattern)
        words.extend(wordList)
        documents.append((wordList, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# Lemmatize and remove unnecessary punctuation
words = [lemmatizer.lemmatize(word.lower()) for word in words if word not in ignoreLetters]
words = sorted(set(words))  # Remove duplicates and sort

classes = sorted(set(classes))  # Remove duplicates and sort

# Save words and classes to pickle files
pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

# Prepare training data
training = []
outputEmpty = [0] * len(classes)

for document in documents:
    bag = []
    wordPatterns = document[0]
    wordPatterns = [lemmatizer.lemmatize(word.lower()) for word in wordPatterns]
    for word in words:
        bag.append(1) if word in wordPatterns else bag.append(0)

    outputRow = list(outputEmpty)
    outputRow[classes.index(document[1])] = 1
    training.append(bag + outputRow)

random.shuffle(training)
training = np.array(training)

# Split training data into input (X) and output (Y)
trainX = training[:, :len(words)]
trainY = training[:, len(words):]

# Build and compile the neural network model
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(128, input_shape=(len(trainX[0]),), activation='relu'))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(64, activation='relu'))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(len(trainY[0]), activation='softmax'))

# Compile the model
sgd = tf.keras.optimizers.SGD(learning_rate=0.01, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

# Train the model
model.fit(np.array(trainX), np.array(trainY), epochs=200, batch_size=5, verbose=1)

# Save the model
model.save('chatbot_model.h5')
print('Model trained and saved successfully!')