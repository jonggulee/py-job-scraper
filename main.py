from flask import Flask, render_template, request
from extractors.wwr import extract_wwr_jobs

app = Flask("JobScrapper")

@app.route("/")
def home():
    return render_template("home.html", name="jake")

db = {}

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword in db:
        jobs = db[keyword]
    else:
        wwr = extract_wwr_jobs(keyword)
        jobs = wwr
        db[keyword] = jobs
    return render_template("search.html", keyword=keyword, jobs=jobs)
 
app.run("0.0.0.0", port=4000)