from flask import redirect, render_template, request, url_for
from flask_login import current_user
from application.auth.models import User

from application import app, db, login_required
from application.materials.models import Material
from application.materials.forms import MaterialForm
from application.courses.models import Course

@app.route("/materials", methods=["GET"])
@login_required(role="ADMIN")
def materials_index():
    return render_template("material/list.html", Material = Material.query.all())

@app.route("/materials/new/", methods=["GET"])
@login_required(role="ADMIN")
def materials_form():
    c = Course.query.all()
    names=[(i.id, i.name) for i in c]
    form = MaterialForm()
    form.Course.choices = names
    return render_template("materials/new.html", form = form)

@app.route("/materials/", methods=["POST"])
@login_required(role="ADMIN")
def material_create():
    c = Course.query.all()
    names=[(i.id, i.name) for i in c]
    form= MaterialForm(request.form)
    form.Course.choices = names

    if not form.validate():
        return render_template("material/new.html", form = form)
    
    m = Material(form.name.data, form.Course.data)

    db.session().add(m)
    db.session().commit()
  
    return redirect(url_for("courses_index"))

@app.route("/materials/<course_id>", methods=["GET"])
def material_info(course_id):

    material = Material.query.filter_by(id=course_id).first_or_404()
    
    return render_template("materials/material.html", material = material)