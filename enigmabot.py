import random
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from keras.models import load_model
from flask import Flask, request, jsonify
from flask_cors import CORS



# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Download NLTK data if not present
nltk.download('punkt')
nltk.download('wordnet')

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# Load intents
try:
    with open('intents.json', 'r') as f:
        intents = json.load(f)
except FileNotFoundError:
    raise Exception("intents.json file not found. Ensure it is in the working directory.")

# Load words, classes, and model
try:
    words = pickle.load(open('words.pkl', 'rb'))
    classes = pickle.load(open('classes.pkl', 'rb'))
    model = load_model('chatbot_model.h5')
except FileNotFoundError as e:
    raise Exception(f"Required file not found: {e.filename}")

# Function to clean up the sentence and tokenize it
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

# Function to convert the sentence into a bag of words
def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

# Function to predict the class of the sentence
def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return [{'intent': classes[r[0]], 'probability': str(r[1])} for r in results]

# Function to get the response from the intents JSON
def get_response(intents_list, intents_json):
    if not intents_list:
        return "Sorry, I didn't understand that."
    tag = intents_list[0]['intent']
    for intent in intents_json['intents']:
        if intent['tag'] == tag:
            return random.choice(intent['responses'])
    return "Sorry, I didn't understand that."

# Define a route for chatbot interaction
@app.route('/chat', methods=['POST'])
def chat():
    message = request.json.get("message")
    
    if message:
        # Predict the class of the message
        intents_list = predict_class(message)
        
        # Get the bot's response
        response = get_response(intents_list, intents)
        
        return jsonify({"response": response})
    else:
        return jsonify({"response": "Please provide a message!"}), 400
@app.route("/",methods=["GET"])
def main():
    return jsonify({"status": "Running on port 9000"})

if __name__ == "__main__":
    app.run(port=5000, debug=True)