##  Project Overview  
GFGSOLVE is an AI-powered chatbot designed to assist with coding problems. Users can ask coding-related questions, and if the provided solution is not optimal, they can use the **"Not Satisfied"** button to send the query to experts for review. The model retrains itself to improve responses over time.  

## 🗂Project Structure in VSCode  
GFGSOLVE/ # Main Project Folder
│── /static/ # Contains frontend assets (CSS, JS)
│ ├── styles1.css # Login page CSS file
│ ├── script.js # JavaScript file for login page
│── /templates/ # Contains HTML files
│ ├── front.html # Introduction Page
│ ├── enigma.html # Login Page
│ ├── c.html # Chatbot Interface
│ ├── expert.html # Expert Window Page
│── /model/ # AI Model and Data Files
│ ├── chatbot_model.h5 # Trained AI Model
│ ├── intents.json # Data file for chatbot responses
│── app.py # Flask Backend for storing user data
│── server.py # Flask Backend for Expert Window Interface
│── chatbot.py # Model Training Script
│── enigmabot.py # Chatbot API for NLP Processing
│── requirements.txt # Python Dependencies
│── README.md # Project Documentation

1.Install Dependencies
First, ensure you have Python installed, then run:
pip install -r requirements.txt

2. Set Up a Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Run the Flask Applications
python app.py
python server.py
pyhon chatbot.py
python enigmabot.py

