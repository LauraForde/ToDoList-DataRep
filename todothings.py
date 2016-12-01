import flask as flsk
from flask import render_template, request
import sqlite3

app = flsk.Flask(__name__)

DATABASE = 'lists.db'
connDB = sqlite3.connect(DATABASE)
c = connDB.cursor()

@app.route("/")
def route():
    return app.send_static_file('webapp.html')    

#http://flask.pocoo.org/docs/0.11/patterns/sqlite3/
def get_db():
    db = getattr(flsk.g, '_database', None)
    if db is None:
        db = flsk.g._database = sqlite3.connect('lists.db')
    return db 



@app.route("/add", methods = ["GET", "POST"])
def add():

    c.execute('INSERT INTO list(listName, items) VALUES(?, ?)',(flsk.request.form['listName'], flsk.request.form['items'],))

    connDB.commit()
    return str(c.fetchall())       
        
@app.route("/saved", methods = ["GET", "POST"])
def saved():
    
    c.execute("SELECT * FROM list")
    return str(c.fectall())

if __name__ == "__main__":
    app.run()
    