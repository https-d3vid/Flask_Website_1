
from flask import Flask, render_template , request , redirect, url_for, session, flash
from datetime import timedelta


app = Flask("Informatics")
app.secret_key = "Hello" 


@app.route("/")
def Home():
    return render_template('windex.html')

@app.route("/user")
def User():
    if "user" in session:
        user = session["user"]
        return f"<h1> welcome.. {user}</h1>"
    else:
        return redirect(url_for("Signup"))

@app.route("/signup", methods=["POST","GET"])
def Signup():
    if request.method == "POST":
        user = request.form["us"]
        session["user"] = user
        return redirect(url_for("Home"))
    else: 
        if "user" in session:
            return redirect(url_for("User"))    
        return render_template("signup.html")

@app.route("/signin", methods=["POST","GET"])
def Signin():
    if "user" in session:
        return redirect(url_for("Home"))
    else:
        return render_template("signin.html")
    


@app.route("/signout")
def Signout():
    session.pop("user", None)
    flash("You have been logged out","info")
    return redirect(url_for("Signup"))




if __name__ == "__main__":
    app.run(debug=True)