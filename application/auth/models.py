from application import db
from application.models import Base

from sqlalchemy.sql import text

class User(Base):

    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    urole = db.Column(db.String(80), nullable=False)

    tasks = db.relationship("Course", backref='account', lazy=True)
  
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
    def find_users_subscriptions(done='1'):
        stmt = text("SELECT Course.id, Course.name FROM Course"
                     " LEFT JOIN Account ON Course.account_id = Account.id"
                     " WHERE (Course.done = :done)"
                     " GROUP BY Course.id"
                     " HAVING COUNT(*) > 0").params(done=done)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})

        return response