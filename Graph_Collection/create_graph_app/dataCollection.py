import decisionTree as dt
import sys
from flask import Flask, render_template, request, redirect, Response
import random, json

app = Flask(__name__)

@app.route('/')
def output():
	# serve index template
	return render_template('index.html', name='Ese')

@app.route("/loading", methods = ['POST'])
def makeGraph():
    print("makeGraph() in dataCollection.py")
    data = request.get_json()
    gc = GraphCreator(data)
    return gc.generateGraph()

if __name__ == "__main__":
	app.run()

# GraphCreator is a class that generates the 
# decision tree and formulates the graph based
# on the data that is passed into it.
class GraphCreator:
    def _init_(self, data):
        self.data = data
        self.decisionTree = dt.DecisionTree()

    def generateGraph(self):
        tree = self.decisionTree.createDecisionTree()
        answer = self.decisionTree.decisionTreeTest(tree, self.data)
        return answer