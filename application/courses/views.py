from flask import redirect, render_template, request, url_for
from flask_login import current_user
from application.auth.models import User

from application import app, db, login_required
from application.courses.models import Course
from application.courses.forms import CourseForm
from application.auth.models import subs
from application.materials.models import Material

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

    c = course_id
    u = current_user.id

    statement = subs.insert().values(account_id=u, course_id=c)
    db.session.execute(statement)
    db.session.commit()
  
    return redirect(url_for("courses_index"))

@app.route("/courses/", methods=["POST"])
@login_required(role="ADMIN")
def courses_create():
    form = CourseForm(request.form)

    if not form.validate():
        return render_template("courses/new.html", form = form)
    
    name = form.name.data
    description = form.description.data

    c = Course(name, description)
    c.account_id = current_user.id

    db.session().add(c)
    db.session().commit()
  
    return redirect(url_for("courses_index"))

@app.route("/my_courses", methods=["GET"])
def my_courses_index():
    user_id = current_user.id
    return render_template("courses/my_courses.html", my_courses = User.find_users_subscriptions(user_id))

@app.route("/courses_remove/<course_id>/", methods=["DELETE", "GET"])
@login_required(role="ADMIN")
def courses_remove(course_id):

    course_to_delete = Course.query.get_or_404(course_id)

    if course_to_delete.material:
        for material in reversed(course_to_delete.material):
            db.session().commit()
            db.session().delete(material)
            db.session().commit()

    db.session().delete(course_to_delete)
    db.session().commit()
  
    return redirect(url_for("courses_index"))

@app.route("/courses/<course_id>", methods=["GET"])
def course_info(course_id):

    course = Course.query.get_or_404(course_id)
    
    return render_template("courses/description.html", course = course)

@app.route("/courses/edit/<course_id>", methods=["GET"])
@login_required(role="ADMIN")
def courses_editform(course_id):
    courseToEdit = Course.query.get_or_404(course_id)

    form=CourseForm(formdata=request.form, obj=courseToEdit)
    return render_template("courses/edit_course.html", form = form, course_id=course_id)

@app.route("/courses/edit/<course_id>/", methods=["POST"])
@login_required(role="ADMIN")
def edit_course(course_id):

    courseToEdit = Course.query.get_or_404(course_id)

    form=CourseForm(formdata=request.form, obj=courseToEdit)
    
    if form.validate():
        courseToEdit.name=form.name.data
        courseToEdit.description=form.description.data

        db.session().commit()
        return redirect(url_for("courses_index"))
    else:
        return render_template("courses/edit_course.html", form = form)