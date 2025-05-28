from flask import Flask

app=Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
    return"<h1 align=center>WELCOME TO HOMEPAGE<h1>"

if __name__=='__main__':
    app.run(debug=True)