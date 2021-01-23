
# decisionTree.py has a hardcoded decision tree that will help 
# figure out what is the appropriate graph that needs to be created
# based off of the data set given.
# Author: Eseroghene Omene

# Node is a class that will have the feature, and point you to left
# and right nodes based off of the answer to the feature. If the node
# is a leaf node, then it will instead have the guess of what graph 
# will be needed for the data set
class Node:
    def _init_(self, feature, guess, leftNode, rightNode):
        self.feature = feature
        self.guess = guess
        self.leftNode = leftNode
        self.rightNode = rightNode

# DecisionTree is the class that will have the hardcoded information
# to create the decision tree using the Node class. DecisionTree will
# also have a function that will actually generate the answer to what
# graph will be needed based off the data set
class DecisionTree:
    def _init_(self, data, features):
        self.data = data;
        self.features = features;
    
    # method that hardcodes the tree
    def createDecisionTree(self):
        leaf1a = Node(None, "Line Graph || Bar Graph", None, None)
        leaf1b = Node(None, "Bar Graph || Circle Graph", None, None)
        leaf1c = Node(None, "Circle Graph", None, None)
        leaf2a = Node(None, "Line Graph", None, None)
        leaf2b = Node(None, "Double Bar Graph || Line Graph", None, None)
        node3 = Node(IsThereACorrelationBetweenTwoColumns(), None, leaf2a, leaf2b)
        node2b = Node(HowManyCategoriesInColumn(2), None, leaf1b, leaf1c)
        node2a = Node(HowManyCategoriesInColumn(1), None, leaf1a, node3)
        node1 = Node(DoesDataHaveATimeInterval(), None, node2a, node2b)
        return None

    def decisionTreeTest(self, tree, data):
        # tree = the decision tree that was created as a result of the decisionTreeTrain() method
        # testPoint = a method that asks a question testing the likelihood of a dataset belonging to a certain graph
        # create a way to simulate tha for each testPoint, you get closer and closer to the correct answer of what the graph should be
        if tree.leftNode == None and tree.rightNode == None:
            # we are at the leaf
            return tree.guess
        else:
            # we are at a parent node
            guess = tree.feature.answerQuestion(data)
            if guess == "LEFT":
                # we go left
                return self.decisionTreeTest(tree.leftNode, data)
            elif guess == "RIGHT":
                # we go right
                return self.decisionTreeTest(tree.rightNode, data)
        return None

# Feature is a interface that will act as the crossroads before
# breaking off into different paths in the decision tree. Features
# in a decision tree are generally nodes that ask a question that helps the
# algorithm visualize what the correct guess is (the same way you would
# ask someone to describe a banana if you had never seen it, by inquiring of its'
# FEATURES). The instance of the Feature class will be present in every parent 
# node, but not the leaf nodes.
class Feature:
    def _init_(self):
        self.answers = ["LEFT", "RIGHT"] # we are using LEFT and RIGHT because as of right now, the decision trees are not divided into more than 2 branches
    
    # this is the function each instance of the interface will have to make on their own
    def answerQuestion(self, data):
        pass

# DoesDataHaveATimeInterval is a class that implements the
# Feature interface. This class will answer the question
# of whether or not the data set has a time interval.
class DoesDataHaveATimeInterval(Feature):
    def _init_(self):
        self.YES = 0
        self.NO = 1

    def answerQuestion(self, data):
        # check the data for a column that represents a date/time
        # check whether or not the date column varies enough to be considered
        # TODO: Write Code
        return self.answers[self.YES]

# HowManyCategoriesInColumn is a class that implements the 
# Feature interface. This class will answer how many different
# values are in a particular column (that has value type string)
class HowManyCategoriesInColumn(Feature):
    def _init_(self, threashold):
        self.threadhold = threashold
        self.THREASHOLD = 0
        self.MORE_THAN_THREASHOLD = 1
    
    def answerQuestion(self, data):
        # check for the first column that does not have integer value and is not a date
        # check how many row values differ from each other in that column
        # determine if the amount is equal to the threashold or more than the threashold
        # check all columns and update if answer improves
        # TODO: Write Code
        return self.answers[self.THREASHOLD]

# IsThereACorrelationBetweenTwoColumns is a class that implements the
# Feature interface. This class will answer if there are any coorelation
# between two columns.
class IsThereACorrelationBetweenTwoColumns(Feature):
    def _init_(self):
        self.YES = 0
        self.NO = 1
    
    def answerQuestion(self, data):
        # find two columns in the data set that have a non string value or non date value
        # determine if there is a positive, negative, or no coorelation between the columns.
        # check all columns and update if answer imporves
        # TODO: Write Code
        return self.answers[self.YES]