import flask as flsk
import sqlite3

DATABASE = 'lists.db'
connDB = sqlite3.connect(DATABASE)
c = connDB.cursor()

app = flsk.Flask(__name__)

#http://flask.pocoo.org/docs/0.11/patterns/sqlite3/
def set_up():
    db = getattr(flsk.g, '_database', None)
    if db is None:
        db = flsk.g._database = sqlite3.connect(DATABASE)
    return db    

@app.route("/")
def root():
    c = set_up().cursor()
    return app.send_static_file('webapp.html')    

@app.route("/addList", methods = ["GET", "POST"])
def addList():
    c.execute("INSERT INTO lists VALUES(?, ?, ?, ?)",(flsk.request.form['listName'], flsk.request.form['item1'], flsk.request.form['item2'], flsk.request.form['item3']))

    connDB.commit()
    return str(c.fetchall())       
        
@app.route("/saved", methods = ["GET", "POST"])
def saved():
    
    c.execute("SELECT * FROM list")
    return str(c.fectall())

@app.teardown_appcontext
def close_connection(execption):
    db = getattr(flsk.g, '_database', None)
    if db is not None:
        db.close()
        
if __name__ == "__main__":
    app.run()
    