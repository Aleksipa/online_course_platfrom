from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.courses.models import Course
from application.courses.forms import CourseForm


@app.route("/courses", methods=["GET"])
def courses_index():
	return render_template("courses/list.html", courses = Course.query.all())

@app.route("/courses/new/")
@login_required
def courses_form():
    return render_template("courses/new.html", form = CourseForm())

@app.route("/courses/<course_id>/", methods=["POST"])
@login_required
def courses_set_done(course_id):

    t = Course.query.get(course_id)
    t.done = True
    db.session().commit()
  
    return redirect(url_for("courses_index"))

@app.route("/courses/", methods=["POST"])
@login_required
def courses_create():
    form = CourseForm(request.form)

    if not form.validate():
        return render_template("courses/new.html", form = form)
    
    t = Course(form.name.data)
    t.account_id = current_user.id

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("courses_index"))