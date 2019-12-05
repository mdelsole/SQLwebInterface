from flask import Flask, render_template, request
from sql_queries import *

app = Flask(__name__)

# Main page


@app.route('/')
def index():
    results = sql_query('SELECT * FROM FLOWERS')
    return render_template('home.html', flowers=results)

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

# Run the app


if __name__ == '__main__':
    app.run(debug=True)