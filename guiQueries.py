from flask import Flask, render_template, request
from sqlHandler import *
import csv
from csvEditor import *


app = Flask(__name__)


# Main page
@app.route('/')
def index():
    # Read in the flowers table
    results = sql_query('SELECT * FROM FLOWERS')
    return render_template('home.html', flowers=results, images=readCSV())


# Router for more complex queries (Requirement 1: Query)
@app.route('/select', methods=['POST', 'GET'])
def select():
    comname = request.args.get('comname')
    results = sql_varQuery('SELECT * '
               'FROM SIGHTINGS '
               'WHERE NAME = ? '
               'ORDER BY sighted DESC '
               'LIMIT 10', (comname,))
    theFlowers = sql_query('SELECT * FROM FLOWERS')

    return render_template('home.html', flowers=theFlowers, theResults=results, images=readCSV())


# Pre insert to know what visual panel to show
@app.route('/pre_insert', methods=['POST', 'GET'])
def pre_insert():
    results = sql_query('SELECT * FROM FLOWERS')
    return render_template('home.html', flowers=results, images=readCSV(), shouldShowInsert=True)


# Perform insert (Requirement 3: Insert)
@app.route('/insert', methods=['POST', 'GET'])
def insert():
    # Retrieve the information from the html form
    name = request.form['n']
    person = request.form['p']
    location = request.form['l']
    sighted = request.form['s']

    # Perform the update query
    sql_modify('INSERT INTO SIGHTINGS (NAME, PERSON, LOCATION, SIGHTED) '
               'VALUES(?,?,?,?)', (name, person, location, sighted))

    # Return the flowers table
    results = sql_query('SELECT * FROM FLOWERS')
    return render_template('home.html', flowers=results, images=readCSV(), insertSuccessful=True)


# Fill in placeholder info to be edited
@app.route('/pre_update', methods=['POST', 'GET'])
def pre_update():
    genus = request.args.get('genus')
    species = request.args.get('species')
    comname = request.args.get('comname')
    theIndex = int(request.args.get('theIndex'))
    results = sql_query('SELECT * FROM FLOWERS')
    return render_template('home.html', flowers=results, images=readCSV(), shouldShowUpdate=True,
                           theGenus=genus, theSpecies=species, theComname=comname, theIndex=theIndex)


# Perform update
@app.route('/update', methods=['POST', 'GET'])
def update():
    # Retrieve the information from the html form
    genus = request.form['g']
    species = request.form['s']
    comname = request.form['c']
    image = request.form['i']

    # Retrieve the information of the entry we are updating
    oldGenus = request.args.get('oldGenus')
    oldSpecies = request.args.get('oldSpecies')
    oldComname = request.args.get('oldComname')
    theIndex = int(request.args.get('theIndex'))

    # Update the flowers table
    sql_modify('UPDATE FLOWERS '
               'SET GENUS = ?, SPECIES = ?, COMNAME = ? '
               'WHERE GENUS = ? AND SPECIES = ? AND COMNAME = ?', (genus, species, comname, oldGenus, oldSpecies, oldComname))

    # Update the flower in the sightings table
    sql_modify('UPDATE SIGHTINGS '
               'SET NAME = ? '
               'WHERE NAME = ?', (comname, oldComname))

    # Update our image csv
    updateCSV(theIndex, image)

    # Return the flowers table
    results = sql_query('SELECT * FROM FLOWERS')
    return render_template('home.html', flowers=results, images=readCSV())


# Router for delete
@app.route('/delete', methods=['POST', 'GET'])
def delete():
    if request.method == 'GET':
        genus = request.args.get('genus')
        species = request.args.get('species')
        comname = request.args.get('comname')
        sql_modify('DELETE FROM FLOWERS '
                   'WHERE GENUS = ? AND SPECIES = ? AND COMNAME = ?', (genus, species, comname))

    results = sql_query('SELECT * FROM FLOWERS')

    # Delete the image from the csv
    theIndex = int(request.args.get('theIndex'))
    deleteCSV(theIndex)

    return render_template('home.html', flowers=results, images=readCSV())


# Read in the images of flowers
def readCSV():
    with open("flowersImages.csv", 'r') as my_file:
        reader = csv.reader(my_file, delimiter='\t')
        listOfImages = list(reader)
    return listOfImages


# Run the app
if __name__ == '__main__':
    app.run(debug=True)