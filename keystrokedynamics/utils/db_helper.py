"""Help to create/read/write to SQLite database."""

import sqlite3

def create_db():


def is_table_exists(name):
    conn = sqlite3.connect('keystroke.sqlite')
    cur = conn.cursor()
    name = str(name.replace(" ", ""))
    cur.execute("SELECT * FROM sqlite_master WHERE type='table' AND name=?", (name,))
    row = cur.fetchone()
    cur.close()
    if row is not None:
        print "Username alredy exists"
        return True
    else:
        return False

def insert(prof):
    table  = "".join(prof.keys())
    conn = sqlite3.connect('keystroke.sqlite')
    cur = conn.cursor()

    if is_table_exists(table):
        return False

    cur.execute('''
    CREATE TABLE IF NOT EXISTS ''' + table +''' (digraph_id INTEGER, expected_value REAL, variance REAL, frequency INTEGER)''')
    keys = prof["".join(prof.keys())].getkeys()
    values = prof["".join(prof.keys())].getvalues()
    for i in xrange(len(keys)):
        cur.execute('''INSERT INTO ''' + table +''' (digraph_id, expected_value, variance, frequency)
        VALUES ( ?, ?, ?, ? )''', (keys[i], values[i][0], values[i][1], values[i][2]))
    conn.commit()
    cur.close()
    return True
