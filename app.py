# app.py
from flask import Flask, render_template, request
import main

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', message=main.welcome_message())

@app.route('/run', methods=['POST'])
def run():
    answer = request.form['command']
    result = main.process_input(answer)  # Process the user input
    return result

if __name__ == '__main__':
    app.run(debug=True)
