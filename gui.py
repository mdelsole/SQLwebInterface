from flask import Flask, render_template, request
from sql_queries import *
import csv


app = Flask(__name__)

# For images of the flowers
with open("flowersImages.csv", 'r') as my_file:
    reader = csv.reader(my_file, delimiter='\t')
    listOfImages = list(reader)

# Main page


@app.route('/')
def index():
    results = sql_query('SELECT * FROM FLOWERS')
    return render_template('home.html', flowers=results, images=listOfImages)

# Router for delete


@app.route('/delete', methods=['POST', 'GET'])
def delete():
    if request.method == 'GET':
        genus = request.args.get('genus')
        species = request.args.get('species')
        comname = request.args.get('comname')
        sql_delete('DELETE FROM FLOWERS '
                   'WHERE GENUS = ? AND SPECIES = ? AND COMNAME = ?', (genus, species, comname))
    results = sql_query('SELECT * FROM FLOWERS')
    return render_template('home.html', flowers=results)


@app.route('/select', methods=['POST', 'GET'])
def select():
    if request.method == 'GET':
        genus = request.args.get('genus')
        species = request.args.get('species')
        comname = request.args.get('comname')
        sql_update('SELECT *'
                   'FROM SIGHTINGS '
                   'WHERE GENUS = ? AND SPECIES = ? AND COMNAME = ?'
                   'ORDER BY sighted DESC'
                   'LIMIT 10', (genus, species, comname))
    results = sql_query('SELECT * FROM FLOWERS')
    return render_template('home.html', flowers=results)

# Run the app


if __name__ == '__main__':
    app.run(debug=True)