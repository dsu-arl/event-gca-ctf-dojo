#!/usr/bin/exec-suid -- /usr/bin/python3 -I

from flask import Flask, render_template, make_response, request
import base64
from secrets import token_hex

app = Flask(__name__)
app.secret_key = token_hex(32)

try:
    with open('/flag', 'r') as fObj:
        flag = fObj.read()
except Exception as e:
    print(e)
    print("Unable to read flag from '/flag'!")
    exit(0)

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
    if not isadmin: # initial setup
        isadmin = False
        resp = make_response(render_template("admin.html", isadmin=isadmin))
        resp.set_cookie("isadmin", base64.b64encode(b"no").decode('utf-8'))
        return resp
    else:
        try:
            isadmin = True if base64.b64decode(isadmin) == b"yes" else False
        except:
            isadmin = False
        return render_template("admin.html", flag=flag, isadmin=isadmin)

if __name__ == "__main__":
    app.run()
