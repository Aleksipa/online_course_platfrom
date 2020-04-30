from application import db
from application.models import Base
from sqlalchemy.sql import text
from application.courses.models import Course
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, backref


subs = db.Table('subs',
    db.Column('account_id', db.Integer, db.ForeignKey('account.id')),
    db.Column('course_id', db.Integer, db.ForeignKey('course.id'))
)

class User(Base):

    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    urole = db.Column(db.String(80), nullable=False)

    courses = db.relationship("Course", backref='account', lazy=True)
    subscriptions = db.relationship("Course", secondary=subs, backref=db.backref('subscribers', lazy = 'dynamic'))
  
    def __init__(self, name, username, password, urole):
         self.name = name
         self.username = username
         self.password = password
         self.urole = urole

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def get_urole(self):
            return self.urole

    @staticmethod
    def find_users_subscriptions(user_id):
        stmt = text("SELECT Course.id, Course.name FROM Course "
        + " LEFT JOIN Subs ON Course.id = Subs.course_id "
        + " LEFT JOIN Account ON Account.id = Subs.account_id "
        + " WHERE Subs.account_id = :user_id "
        + " GROUP BY Course.id").params(user_id=user_id)

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})

        return response