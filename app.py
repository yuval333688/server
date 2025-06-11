from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"



@app.route("/getNames")
def getNames():
    print("getNames called\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    names = ["James", "Mary", "John", "Patricia", "Robert", "Jennifer", "Michael", "Linda", "William", "Elizabeth"]
    return jsonify(names)