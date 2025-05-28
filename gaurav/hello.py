from flask import Flask

app=Flask(__name__)

@app.route("/")
@app.route("/home")
def greet():
    return"<h1 align=center>WELCOME TO HOMEPAGE<h1>"

@app.route("/about")
@app.route('/about/<name>') #parameter being sent
def about(name="page"): #if parameter is not sent then page will be sent
    return f"About {name}"

if __name__=='__main__':
    app.run(debug=True)