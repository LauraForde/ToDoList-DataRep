import flask as flsk
import sqlite3

DATABASE = 'lists.db'

app = flsk.Flask(__name__)

#http://flask.pocoo.org/docs/0.11/patterns/sqlite3/
def get_db():
    db = getattr(flsk.g, '_database', None)
    if db is None:
        db = flsk.g._database = sqlite3.connect(DATABASE)
    return db    

@app.route("/")
def root():
    return app.send_static_file('webapp.html')    

@app.route("/add", methods = ["GET", "POST"])
def addAList():
    item1 = flsk.request.values["item1"]
    item2 = flsk.request.values["item2"]
    item3 = flsk.request.values["item3"]
    
    db = sqlite3.connect('lists.db')
    c = db.cursor()

    c.execute("INSERT INTO list VALUES(?, ?, ?, ?)",(listName, item1, item2, item3))

    db.commit()
    db.close()
    
@app.teardown_appcontext
def close_connection(execption):
    db = getattr(fl.g, '_database', None)
    if db is not None:
        db.close()
        
@app.route("/")
def hello():
    c = get_db().cursor()
    c.execute("SELECT listName FROM list")
    return str(c.fectall())
        
if __name__ == "__main__":
    app.run()
    