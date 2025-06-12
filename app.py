from flask import Flask, jsonify
from DataBaseManager import DataBaseManager
import os
app = Flask(__name__)
dataBaseManager = DataBaseManager()




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
    borders = dataBaseManager.getCountryBorder(country)
    return jsonify(borders)

if __name__ == '__main__':
    # Initialize Supabase client
    dataBaseManager 
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


