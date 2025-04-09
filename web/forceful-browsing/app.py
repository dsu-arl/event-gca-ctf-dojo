#!/usr/bin/exec-suid -- /usr/bin/python3 -I
from flask import Flask, render_template, redirect

app = Flask(__name__)

try:
    with open('/flag', 'r') as fObj:
        flag = fObj.read()
except Exception as e:
    print(e)
    print("Unable to read flag from '/flag'!")
    exit(0)

pages = {
    1: {"name": "Page One", "visible": True, "content": "This is our first post ever! Woo!"},
    2: {"name": "Page Two", "visible": True, "content": "This is our second post. It's about as interesting as the first"},
    3: {"name": "Page Three", "visible": True, "content": "This is our third and last post - nothing else to see here ;)"},
    7: {"name": "Hidden Page", "visible": False, "content": flag},
}

@app.route("/")
def home():
    return render_template("home.html", pages=pages)

@app.route("/p/<int:id>")
def page(id=None):
    if not id or id not in pages:
        return "Page not found", 404
    return render_template("page.html", page=pages[id])

if __name__ == "__main__":
    app.run()
