# Importing couchdb
import couchdb

# Setting up server
couch = couchdb.Server('http://127.0.0.1:5984/')

# Creating database called list
db = couch.create('list')