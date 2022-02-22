from pydoc import render_doc
from flask import Flask, render_template
import pymongo


ATLAS_CONN_STR = "mongodb://root:Password123@cluster0-shard-00-00.nodgm.mongodb.net:27017,cluster0-shard-00-01.nodgm.mongodb.net:27017,cluster0-shard-00-02.nodgm.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-4a3bnn-shard-0&authSource=admin&retryWrites=true&w=majority"
client = pymongo.MongoClient(ATLAS_CONN_STR)
myDb = client.cluster0

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/league/<int:leagueNumber>/contest/<int:contestNumber>')
def contest(leagueNumber, contestNumber):
    contestCollection = myDb[f'contest_{contestNumber}']
    contestData = contestCollection.find()
    return render_template('contest.html',leagueNumber=leagueNumber, contestNumber=contestNumber, contestData = contestData)

app.run(debug=True)