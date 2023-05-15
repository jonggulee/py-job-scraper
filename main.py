from flask import Flask, render_template

app = Flask("JobScrapper")

@app.route("/")
def home():
    return render_template("home.html", name="jake")

@app.route("/search")
def hello():
    return render_template("search.html")
 
app.run("0.0.0.0", port=4000)