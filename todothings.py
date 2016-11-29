import flask as flsk
import sqlite3

DATABASE = 'lists.db'

app = flsk.Flask(__name__)

#http://flask.pocoo.org/docs/0.11/patterns/sqlite3/
def loadDB():
    db = getattr(flsk, '_database', None)
    if db is None:
        db = flsk._database = sqlite3.connect(DATABASE)
    return db    

@app.route("/")
def root():
    return app.send_static_file('webapp.html')    

@app.route("/add", methods = ["GET", "POST"])
def addAList():
    listName = flsk.request.values["listName"]
    item1 = flsk.request.values["item1"]
    item2 = flsk.request.values["item2"]
    item3 = flsk.request.values["item3"]
    
db = sqlite3.connect('lists.db')
c = db.cursor()

c.execute("INSERT INTO list VALUES(?, ?, ?, ?)",(listName, item1, item2, item3))

db.commit()
db.close()


if __name__ == "__main__":
    app.run()
    