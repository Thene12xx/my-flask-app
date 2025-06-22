import os
from flask import Flask, render_template

# Set the Flask app and templates folder
app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

# This block is ignored by Gunicorn (used only for local testing)
if __name__ == '__main__':
    app.run(debug=True)
