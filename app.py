from flask import Flask, render_template, request, url_for, redirect, session

app = Flask(__name__)

@app.route("/")
def home():
    return "Home Page"


if __name__ == '__main__':
    app.run(debug=True)