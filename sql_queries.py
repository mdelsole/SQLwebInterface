import sqlite3


DATABASE = '/Users/Michael/Documents/Python Projects/Database/flowers2019.db'

# Make a convenience function for running SQL queries


def sql_query(query):
    connection = sqlite3.connect(DATABASE)
    cur = connection.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    return rows


def sql_update(query,var):
    connection = sqlite3.connect(DATABASE)
    cur = connection.cursor()
    cur.execute(query,var)
    connection.commit()


def sql_delete(query,var):
    connection = sqlite3.connect(DATABASE)
    cur = connection.cursor()
    cur.execute(query,var)
    connection.commit()