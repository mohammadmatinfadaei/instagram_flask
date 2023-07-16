from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SECRET_KEY']='jhvhijghlkbvhjvjkjhvcj'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///name.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)
class Users(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.Text)
    password = db.Column(db.Text)


    
    def __repr__(self):
        return f'acant({self.id},{self.username},{self.password})'

class Follow(db.Model):
    id=db.Column(db.Integer,primary_key=True)
   
    follower= db.Column(db.Text)
    following= db.Column(db.Text)

    
    def __repr__(self):
        return f'acant({self.id},{self.follower},{self.following})'


class post(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    poster = db.Column(db.Text)

    text= db.Column(db.Text)
    Picture = db.Column(db.Text)

    def __repr__(self):
        return f'post({self.id},{self.poster},{self.text},{self.Picture})'


class likes(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_like = db.Column(db.Text)
    post_like = db.Column(db.Text)


    def __repr__(self):
        return f'likes({self.id},{self.user_like},{self.post_like})'



class id(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    id_pic = db.Column(db.Text)
  


    def __repr__(self):
        return f'id({self.id},{self.id_pic})'
        
class direct(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    person_one = db.Column(db.Text)
    person_two = db.Column(db.Text)
    message = db.Column(db.Text)

    def __repr__(self):
        return f'send_m({self.person_one},{self.person_two},{self.message})'

