from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import login_required


app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Database
db = SQL("sqlite://phonebook.db")

# Initial Route
@app.route("/")
def log_into():
    return render_template("login.html")


# Register
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "GET":
        return render_template("register.html")

    #Register user
    else:
        # Values
        name = request.form.get("username").upper()
        email = request.form.get("useremail").lower()
        number = request.form.get("usernumber")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")


        # Validate email
        if not email:
            return render_template("error.html", message="Invalid Email")
        # Validate name
        if not name:
            return render_template("error.html", message="Invalid Name")
        # Validate number
        if not number:
            return render_template("error.html", message="Invalid Number")
        # Validate password
        if not password:
            return render_template("error.html", message="Invalid Password")
        # Validate confirmation
        if not confirmation:
            return render_template("error.html", message="Invalid Confirmation")
        # Matched confirmation and password
        if confirmation != password:
            return render_template("error.html", message="Confirmation and Password no match")
        # Query database for useremail
        email_db = db.execute("SELECT * FROM users WHERE useremail = ?", request.form.get("useremail"))
        if email_db in db.execute("SELECT * FROM users WHERE useremail"):
            return render_template("error.html", message="User already registered!")
        # Password
        hash = generate_password_hash(password)
        try:
            # User Add
            new_user = db.execute("INSERT INTO users (useremail, hash) VALUES (?, ?)", email, hash)
            new_contact = db.execute("INSERT INTO contacts (usernumber, username) VALUES (?, ?)", number, name)
        except:
            return render_template("error.html", message="User already registered!")

        session["user_id"] = new_user, new_contact

        return render_template("search.html")




# Login
@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()
    # User reached route via GET (as by clicking a link or via redirect)
    if request.method == "POST":
         # Validate email
        if not request.form.get("useremail"):
            return render_template("error.html", message="Invalid Email")
         # Validate password
        elif not request.form.get("password"):
            return render_template("error.html", message="Invalid Password")
        # Query database for useremail
        rows = db.execute("SELECT * FROM users WHERE useremail = ?", request.form.get("useremail").lower())

        # Ensure useremail exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return render_template("error.html", message="invalid useremail and/or password")

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        return render_template("search.html")
    else:
        return render_template("login.html")


# Logout
@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


# Search
@app.route("/search")
@login_required
def search():
    """Contacts search"""
    return render_template("search.html")



# Search Result
@app.route("/list", methods=["GET", "POST"])
@login_required
def list():

    if request.method == "POST":
        user_search = request.form.get("searchname").upper()
        contact = db.execute("SELECT * FROM contacts WHERE username = ?", user_search)

        # Checks if the searched name exists in the database
        if len(contact) != 1 or not request.form.get("searchname"):
            return render_template("error.html", message="Name not found or invalid")

        else:
            # Research data
            name_db = contact[0]["username"]
            number_db = contact[0]["usernumber"]
            return render_template("list.html", name = name_db, number = number_db)


    else:
        return render_template("search.html")




