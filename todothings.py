import flask as fl

app = fl.Flask(__name__)

@app.route("/")
def root():
    return app.send_static_file('webapp.html')

@app.route("/perms", methods=["GET", "POST"])
def perms():
    perms = [''.join(p) for p in
    it.permutations(fl.request.values["userinput"])]
    return '\n'.join(perms)
            

if __name__ == "__main__":
    app.run()