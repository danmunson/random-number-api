import os
from flask import Flask, render_template, request, jsonify
from random import sample
app = Flask(__name__)

MAIN_URL = 'localhost:3000'

def random_sentiment():
    """
    Randomly returns one of {-1,0,1}
    """
    return sample([-1,0,1],1)[0]

@app.route('/')
def index():
    return render_template('index.html', mainUrl=MAIN_URL)

@app.route('/score', methods=['POST'])
def comment_scoring():
    data = request.form
    comment_string, comment_source = data['comment'], data['source']
    return jsonify({'score':random_sentiment()})

if __name__ == '__main__':
    app.run(port=3000)