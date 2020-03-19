from application import app
from flask import render_template, request

@app.route("/courses/new/")
def courses_form():
    return render_template("courses/new.html")

@app.route("/courses/", methods=["POST"])
def courses_create():
    print(request.form.get("name"))
  
    return "hello world!"