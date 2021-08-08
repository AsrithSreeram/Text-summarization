from flask import Flask, render_template, request
import gensim
from gensim.summarization import summarize
from gensim.summarization import keywords

from nltk.sentiment.vader import SentimentIntensityAnalyzer


app = Flask(__name__)


@app.route('/')
def summarizerDashboard():
    return render_template('home.html')


@app.route('/summarizer', methods=['POST'])
def summarizerText():
    text = request.form['summarizer']
    typeOfSummary = request.form['typeOfSummary']
    print(typeOfSummary)
    if typeOfSummary == 'small':
        summary = summarize(text,ratio=0.3)
    elif typeOfSummary == 'medium':
        summary = summarize(text,ratio=0.5)
    else:
        summary = summarize(text,ratio=0.7)


    return render_template('summarizer.html', summary = summary)