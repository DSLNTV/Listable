from flask import Flask, render_template
from pathlib import Path


rootDir = Path.cwd()

app = Flask(__name__, template_folder=rootDir/"frontend")

@app.route("/")
def hello_world():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
