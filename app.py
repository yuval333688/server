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

@app.route("/ChecksIfInCountry/<country>/<latitude>,<longitude>")
def getCountryBorder(country,latitude:float,longitude:float):
    borders = dataBaseManager.getCountryBorder(country)
    from shapely.geometry import Point, Polygon
    point = Point(latitude, longitude)
    polygon = Polygon(borders)
    result = polygon.contains(point)

    return jsonify(result)



