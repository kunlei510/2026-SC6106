#blockchain appliaction
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def index():
    return("welcome to blockchain application")


if __name__ == "__main__":
    app.run()