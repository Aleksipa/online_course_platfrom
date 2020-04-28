from flask import redirect, render_template, request, url_for
from flask_login import current_user
from application.auth.models import User

from application import app, db, login_required
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
def courses_set_subscribe(course_id):

    c = Course.query.get(course_id)
    c.subscribe = True
    db.session().commit()
  
    return redirect(url_for("courses_index"))

@app.route("/courses/", methods=["POST"])
@login_required(role="ADMIN")
def courses_create():
    form = CourseForm(request.form)

    if not form.validate():
        return render_template("courses/new.html", form = form)
    
    c = Course(form.name.data)
    c.account_id = current_user.id

    db.session().add(c)
    db.session().commit()
  
    return redirect(url_for("courses_index"))

@app.route("/my_courses", methods=["GET"])
def my_courses_index():
	return render_template("courses/my_courses.html", my_courses=User.find_users_subscriptions())

@app.route("/courses_remove/<course_id>/", methods=["POST"])
@login_required(role="ADMIN")
def courses_remove(course_id):

    c = Course.query.get(course_id)
    db.session().delete(c)
    db.session().commit()
  
    return redirect(url_for("courses_index"))
