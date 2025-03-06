<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GFGSOLVE - AI-Powered Coding Chatbot</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 40px;
            background-color: #f4f4f4;
            color: #333;
        }
        h1, h2 {
            color: #2c3e50;
        }
        pre {
            background: #e8e8e8;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        code {
            font-family: "Courier New", monospace;
            font-size: 14px;
            color: #e74c3c;
        }
        .container {
            max-width: 900px;
            margin: auto;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
    </style>
</head>
<body>

<div class="container">
    <h1>GFGSOLVE - AI-Powered Coding Chatbot</h1>
    <p>GFGSOLVE is an AI-powered chatbot designed to assist with coding problems. Users can ask coding-related questions, and if the provided solution is not optimal, they can use the <strong>"Not Satisfied"</strong> button to send the query to experts for review. The model retrains itself to improve responses over time.</p>

    <h2>📂 Project Structure in VSCode</h2>
    <pre>
GFGSOLVE/  # Main Project Folder
│── /static/         # Contains frontend assets (CSS, JS)
│   ├── styles1.css   # Login page CSS file
│   ├── script.js     # JavaScript file for login page
│── /templates/      # Contains HTML files
│   ├── front.html    # Introduction Page
│   ├── enigma.html   # Login Page
│   ├── c.html        # Chatbot Interface
│   ├── expert.html   # Expert Window Page
│── /model/          # AI Model and Data Files
│   ├── chatbot_model.h5  # Trained AI Model
│   ├── intents.json  # Data file for chatbot responses
│── app.py           # Flask Backend for storing user data
│── server.py        # Flask Backend for Expert Window Interface
│── chatbot.py       # Model Training Script
│── enigmabot.py     # Chatbot API for NLP Processing
│── requirements.txt # Python Dependencies
│── README.md        # Project Documentation
    </pre>

    <h2>⚙️ Installation & Setup</h2>

    <h3>1. Install Dependencies</h3>
    <p>Ensure you have Python installed, then run:</p>
    <pre><code>pip install -r requirements.txt</code></pre>

    <h3>2. Set Up a Virtual Environment (Optional but Recommended)</h3>
    <pre><code>
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
    </code></pre>

    <h3>3. Run the Flask Applications</h3>
    <pre><code>
python app.py
python server.py
python chatbot.py
python enigmabot.py
    </code></pre>
</div>

</body>
</html>

