#!/usr/bin/exec-suid -- /usr/bin/python3 -I

from flask import Flask, render_template, make_response, request
from secrets import token_hex

app = Flask(__name__)
app.secret_key = token_hex(32)
flag = "temp_flag"


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    return render_template("login.html") # this page isn't functional, it's just presentation of a login page

@app.route("/admin")
def admin():
    # check if user is admin from cookie
    isadmin = request.cookies.get('isadmin', None)
    if not isadmin or isadmin == "0":
        isadmin = False
        resp = make_response(render_template("admin.html", isadmin=isadmin))
        resp.set_cookie("isadmin", "0")
        return resp
    else:
        with open('/flag', 'r') as fObj:
            flag = fObj.read()
        return render_template("admin.html", flag=flag, isadmin=isadmin)

if __name__ == '__main__':
    app.run()
