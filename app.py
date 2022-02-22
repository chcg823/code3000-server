from flask import Flask
import pymongo

app = Flask(__name__)

@app.route('/')
def home():
    pass

@app.route('/league/<int:leagueNumber>/contest/<int:contestNumber>')
def contest(leagueNumber, contestNumber):
    pass

app.run(debug=True)