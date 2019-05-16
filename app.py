import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"



@app.route('/Who let the dogs out')
def hello():
    return 'Woof, woof, woof, woof, woof'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
