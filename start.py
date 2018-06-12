from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/tiide")
def tiide():
    return "Welcome to TIIDE World"

@app.route("/yulwin")
def yulwin():
    return "Yu Yu Lwin"

if __name__ == "__main__":
    app.run()
