import decisionTree as dt
import sys
import json
import requests


# GraphCreator is a class that generates the 
# decision tree and formulates the graph based
# on the data that is passed into it.
class GraphCreator:
    def _init_(self, data):
        self.data = data
        self.decisionTree = dt.DecisionTree()

    def generateGraph(self, data):
        tree = self.decisionTree.createDecisionTree()
        answer = self.decisionTree.decisionTreeTest(tree, data)
        return answer;

# initialize data members to communicate with Node js
url = "http://localhost:3001"
r = requests.get(url)
data = None

# test code to check if code communicates with Node.js
# check if the request is valid
if r.status_code == 200:
    data = r.text
    resp = {
        "Response":200,
        "Message":"Data from Python",
        "Data":data
    }
    print(json.dumps(resp))