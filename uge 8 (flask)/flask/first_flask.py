#!flask/bin/python
from flask import Flask, jsonify, abort, request

app = Flask(__name__)

people = [
    {
        "name" : "jim",
        "id" : 1
    },
    {
        "name" : "luke",
        "id" : 2
    },
    {
        "name" : "jam",
        "id" : 3
    },
    {
        "name" : "hank",
        "id" : 4
    },
    {
        "name" : "lars",
        "id" : 5
    },
    {
        "name" : "juli",
        "id" : 6
    },
    {
        "name" : "luise",
        "id" : 7
    },
    {
        "name" : "julie",
        "id" : 8
    },
    {
        "name" : "kasper",
        "id" : 9
    },
    {
        "name" : "oli",
        "id" : 10
    }
]

@app.route('/')
def index():
    return "Hello, World from flask server!"


@app.route("/datagenerator/api/person/<int:id>", methods=['GET'])
def getPerson(id):

    for person in people:
        if person["id"] == id:
            return jsonify(person)
            

    



if __name__ == '__main__':
    app.run(debug=True)