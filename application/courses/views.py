from application import app, db
from flask import render_template, request
from application.courses.models import Course

@app.route("/courses/new/")
def courses_form():
    return render_template("courses/new.html")

@app.route("/courses/", methods=["POST"])
def courses_create():
    t = Course(request.form.get("name"))

    db.session().add(t)
    db.session().commit()
  
    return "hello world!"