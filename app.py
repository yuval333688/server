from flask import Flask, jsonify
from DataBaseManager import DataBaseManager
app = Flask(__name__)




@app.route("/")
def hello_world():
    return "Hello, World!"



@app.route("/getNames")
def getNames():
    
    print("getNames called\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    names = ["James", "Mary", "John", "Patricia", "Robert", "Jennifer", "Michael", "Linda", "William", "Elizabeth"]
    return jsonify(names)

@app.route("/getCountryBorder/<country>")
def getCountryBorder(country):
    borders = DataBaseManager.instance.getCountryBorder(country)
    return jsonify(borders)

if __name__ == '__main__':
    # Initialize Supabase client
    dataBaseManager = DataBaseManager()
