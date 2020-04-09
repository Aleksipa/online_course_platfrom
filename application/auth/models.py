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
  
    def __init__(self, name, urole):
         self.name = name
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
    def find_users_with_no_subscription(done='0'):
        stmt = text("SELECT Account.id, Account.name FROM Account"
                     " LEFT JOIN Course ON Course.account_id = Account.id"
                     " WHERE (Course.done IS null OR Course.done = :done)"
                     " GROUP BY Account.id"
                     " HAVING COUNT(Course.id) = 0").params(done=done)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})

        return response