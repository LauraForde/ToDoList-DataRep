import sqlite3

DATABASE = 'lists.db'

def setup_db():
    db = sqlite3.connect(DATABASE)
    c = db.cursor()

c.execute("CREATE TABLE IF NOT EXISTS list(listName text, item1 text, item2 text, item3 text, PRIMARY KEY(listName))")

db.commmit()

c.execute("INSERT INTO list(listName, item1, item2, item3) VALUES ('Carrots', 'Steak', 'Spuds')")

db.commit()
db.close()

