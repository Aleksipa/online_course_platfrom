from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, validators

class MaterialForm(FlaskForm):
    name = StringField("Material heading", [validators.Length(min=5)])
    Course = SelectField("Course", coerce=int)
 
    class Meta:
        csrf = False