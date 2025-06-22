import os
from flask import Flask, render_template

# Get the directory of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))

# Set the path to your templates folder
template_path = os.path.join(current_dir, 'templates')

# Create the Flask app with template_folder specified
app = Flask(__name__, template_folder=template_path)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)