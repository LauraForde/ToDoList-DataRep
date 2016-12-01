import sqlite3

DATABASE = 'lists.db'

def setup_db():
    db = sqlite3.connect(DATABASE)
    c = db.cursor()

    c.execute("CREATE TABLE IF NOT EXISTS list(listName text, items text, PRIMARY KEY(listName))")
    db.commit()


    db.close()
    
if __name__ == "__main__":
    setup_db()
    
    
