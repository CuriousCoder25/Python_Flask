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
@app.route("/calculate", methods=["GET","POST"])
def caclulate():
    if request.method=='POST':
        first=int(request.form.get("txt_first"))
        second =int(request.form.get("txt_second"))
        return render_template("calculator.html",sum=first+second)

    return render_template("calculator.html")

@app.route("/contact", methods=["GET","POST"])
def contact():
    if request.method=='POST':
        user_name = request.form.get("name")
        user_email = request.form.get("email")
        return render_template("result.html", name=user_name, email=user_email)
    
    return render_template("contact.html") #this line process the GET method when user first enters /contact

if __name__=='__main__':
    app.run(debug=True)