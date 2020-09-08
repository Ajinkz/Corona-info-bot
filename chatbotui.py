import os
from flask import Flask, render_template
# from flask_ngrok import run_with_ngrok



app = Flask(__name__,static_folder='static')
# run_with_ngrok(app)

@app.route("/")
def index():
    return render_template("index.html", message="Hello Flask!");   


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)