from flask_wtf import FlaskForm
from wtforms import StringField, validators

class CourseForm(FlaskForm):
    name = StringField("Course name", [validators.Length(min=5)])
    description = StringField("Course description", [validators.Length(min=5)])
 
    class Meta:
        csrf = False