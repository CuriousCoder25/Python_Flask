from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/")
@app.route("/home")
def greet():
    # return"<h1 align=center>WELCOME TO HOMEPAGE<h1>"
    return render_template('index.html')

@app.route("/about", methods=['GET','POST'])
@app.route('/about/<name>')          #parameter being sent
def about(name="page"):             #if parameter is not sent then page will be sent
    if request.method=='POST':
        form_name = request.form.get("name")
        return render_template('about.html', name=form_name)
    return render_template('about.html', name=name)    
    # return f"About {name}"    

# @app.route('/login')
# def login():
    
if __name__=='__main__':
    app.run(debug=True)