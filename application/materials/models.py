from application import db
from application.models import Base
from sqlalchemy.sql import text

class Material(Base):

    name = db.Column(db.String(288), nullable=False)

    course_id = db.Column(db.Integer, db.ForeignKey('course.id'),
                           nullable=True)

    def __init__(self, name, c):
        self.name = name
        self.course_id = c