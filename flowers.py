import sqlite3
connection = sqlite3.connect('flowers2019.db')
# Lets us interact with database
cursor = connection.cursor()

# Place queries in here
# cursor.execute()