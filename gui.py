from flask import Flask, render_template, g
import sqlite3


app = Flask(__name__)
DATABASE = '/Users/Michael/Documents/Python Projects/Database/flowers2019.db'


def connect_db():
    return sqlite3.connect(DATABASE)


# Main page


@app.route('/')
def index():
    g.db = connect_db()
    # Execute a SQL command
    cursor = g.db.execute('SELECT * FROM FLOWERS')
    # Put the data into a dictionary
    flowers = [dict(GENUS=row[0], SPECIES=row[1], COMNAME=row[2]) for row in cursor.fetchall()]
    g.db.close()
    # Pass the dictionary into the html to be displayed in a table
    return render_template('home.html', flowers=flowers)


# Run the app


if __name__ == '__main__':
    app.run(debug=True)