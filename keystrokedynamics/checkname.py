import sqlite3

def is_record_exists(name):
    conn = sqlite3.connect('keystroke.sqlite')
    cur = conn.cursor()
    name = str(name.replace(" ", ""))
    cur.execute("SELECT * FROM sqlite_master WHERE type='table' AND name=?", (name,))
    row = cur.fetchone()
    cur.close()
    if row is not None:
        return True
    else:
        return False
