from flask import Flask, render_template, request, url_for, redirect, session

app = Flask(__name__)

# add db connection

# make db models

# start adding login to db

@app.route("/")
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)