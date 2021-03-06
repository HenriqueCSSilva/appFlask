from app import db , manager
from flask_login import LoginManager 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column,Integer,String,ForeignKey,DateTime,Time,Boolean


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(Integer, primary_key=True)
    username = db.Column(String(80), unique=True)
    password = db.Column(String(20))
    name = db.Column(String(20))
    email =  db.Column(String(50), unique=True)


    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True
    
    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)
    
    
    

    def __init__(self, username, password,name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    def __repr__(self):
       return "<User %r>" % self.username


class Post(db.Model):
    __tablename__ = "posts"
    
    id = db.Column(Integer, primary_key=True)
    content = db.Column(db.String(512))
    user_id = db.Column(Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', foreign_keys=user_id)

    def __init__(self, content, user_id):
        self.content = content
        self.user_id = user_id

    def __repr__(self):
       return "<Post %r>" % self.id
   

class Follow(db.Model):
    __tablename__ = "follow"

    id = db.Column(Integer, primary_key = True)
    user_id = db.Column(Integer, db.ForeignKey('users.id'))
    follower_id = db.Column(Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', foreign_keys=user_id)
    follower  = db.relationship('User', foreign_keys=follower_id)


    



