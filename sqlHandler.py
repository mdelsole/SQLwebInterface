import sqlite3


DATABASE = 'flowers2019.db'

# Make a standard SELECT query
def sql_query(query):
    connection = sqlite3.connect(DATABASE)
    cur = connection.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    return rows


# Make a more complex SELECT query that requires variables
def sql_varQuery(query, var):
    connection = sqlite3.connect(DATABASE)
    cur = connection.cursor()
    cur.execute(query, var)
    rows = cur.fetchall()
    return rows


# Perform any modifications to the table, such as UPDATE or INSERT
def sql_modify(query,var):
    connection = sqlite3.connect(DATABASE)
    cur = connection.cursor()
    cur.execute(query,var)
    connection.commit()


# Extra credit: Create a trigger to log insertions, updates, and deletions from all tables
def triggerLog():
    connection = sqlite3.connect(DATABASE)
    cur = connection.cursor()
    cur.execute('CREATE TABLE flower_audit('
                'change_ID INTEGER PRIMARY KEY, '
                'genus VARCHAR(255), '
                'species VARCHAR(255), '
                'comname VARCHAR(255), '
                'name VARCHAR(255), '
                'person VARCHAR(255), '
                'location VARCHAR(255), '
                'sighted VARCHAR(255), '
                'operation CHAR(3));')
    cur.execute('CREATE TRIGGER trigUPD_flowers AFTER UPDATE ON FLOWERS'
                'BEGIN'
                'INSERT INTO flower_audit (genus, species, comname, operation)'
                'VALUES (NEW.genus, NEW.species, NEW.comname, "UPD");'
                'END;')
    cur.execute('CREATE TRIGGER trigDEL_flowers AFTER UPDATE ON FLOWERS'
                'BEGIN'
                'INSERT INTO flower_audit (genus, species, comname, operation)'
                'VALUES (old.genus, old.species, old.comname, "DEL");'
                'END;')
    cur.execute('CREATE TRIGGER trigINS_sightings AFTER UPDATE ON SIGHTINGS'
                'BEGIN'
                'INSERT INTO flower_audit (name, person, location, sighted, operation)'
                'VALUES (NEW.name, NEW.person, NEW.location, NEW.sighted, "INS");'
                'END;')
    connection.commit()
