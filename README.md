## SAGE 3 Graph Generator Project

## Purpose
The purpose of this project is to formulate a creative way to handle data sheets. One thing that Luc Renambot suggested was to “Imagine you get a new dataset that you don't know anything about and want to make some graph”. In other words, this project will be me figuring out how to dynamically create graphs depending on the data set.

## Requirements
* Project must be interactive (create a UI/front end)
* Project must be able to generate different types of graphs (React-window, React-table, Antd, etc)
* Project must be able to determine what graph to generate based off the data set (algorithmic process, possibly utilize machine learning techniques)

## Resources
* ## Python
    I want to use python because they are better for machine learning algorithms and handling large data sets. Also there might be a way to communicate with javascript using python, so if I can use this programming language to talk to the javascript code responsible for the front/back end, I can create a somewhat powerful application.
* ## Node.js
    I want to use Node.js because it is hard to communicate with python using React.js (I’m honestly not too sure of the specifics, but when I tried to import spawn, it didn’t work. Need to do further research on that).

## Diagram
* ## Select File From Computer
    In order for the conversion process to begin, the user must first need to select a file that they want to see a graphical representation of. For now, the file selector in javascript will only be accepting .txt files (because csv can be represented by .txt files). The user needs to select this from the user’s computer, which will then be uploaded into the site.
* ## Submit File for Graph Conversion
    This use case will be represented by a button on the application. But this use case needs to ensure other things before it can start this
* ## Verify File is Chosen
    The application will check if there is a .txt file in the selector before trying to convert anything. If not, it will display an error message. If so, it will continue with the conversion process.
* ## Display Error Page
    The application will tell the user that there was a problem with the file chosen and that they should select a proper file to be converted.
* ## Convert Data to Graph
    The application will perform the machine learning techniques using python to figure out what graph should be used based on the data. Either there is enough data to create a graph, or there isn’t enough data to create a graph.
Display Not Enough Data for Graph
    If there isn’t enough data for the graph (example, if the .txt file is more of a paragraph or word document than an actual csv) then the application will let you know that there isn’t enough data to create a graph from it.
* ## Display Graph
    If there is enough data to create a graph, it will formulate the graph and display it on the screen.
