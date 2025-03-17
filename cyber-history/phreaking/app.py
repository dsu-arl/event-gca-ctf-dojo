from flask import Flask, render_template

app = Flask(__name__)

def getFlagObs():
    with open('/flag', 'r') as fp:
      flag = fp.read()
    key = 41
    obfuscated = ''.join([chr(ord(i)^key) for i in flag])
    return obfuscated

@app.route('/')
def index():
    return render_template("index.html", flag=getFlagObs())

if __name__ == '__main__':
    app.run()