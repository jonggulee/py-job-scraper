from flask import Flask, render_template, request
from extractors.wwr import extract_wwr_jobs

app = Flask("JobScrapper")

@app.route("/")
def home():
    return render_template("home.html", name="jake")

@app.route("/search")
def hello():
    keyword = request.args.get("keyword")
    wwr = extract_wwr_jobs(keyword)
    jobs = wwr
    return render_template("search.html", keyword=keyword, jobs=jobs)
 
app.run("0.0.0.0", port=4000)