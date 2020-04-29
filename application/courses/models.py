from application import db
from application.models import Base
from sqlalchemy.sql import text
from sqlalchemy.orm import relationship, backref

class Course(Base):

    name = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(288), nullable=False)
    subscribe = db.Column(db.Boolean, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    
    material = db.relationship("Material", backref='course', lazy=True)


    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.subscribe = False
