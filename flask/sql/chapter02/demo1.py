# -*- coding: utf-8 -*-
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1:3303/book?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True
db=SQLAlchemy(app)

"""
    create database book default character set utf8;
    1.创建book数据库
    mysql> create database book;
    Query OK, 1 row affected (0.03 sec)
    
"""

"""
    كىتاب ۋە يازغۇچنىڭ ModelClass  نى لاھىيلەش
    يازغۇچنىڭ id , name قاتارلىق خاسلىق بولىدۇ .
    بۇ يازغۇچى بىر نەچچە كىتابنىڭ ئاپتۇرى بولغان بۇلۇشى مۇمكىن .
    شوڭا بۇ modelClass Author بولسا ModelClass Book بىلەن باغلنىشلىق مۇناسۋەتتە بولىدۇ.
"""
class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    books=db.relationship("Book",backref="author")
    pass

class Book(db.Model):
    __tablename__ = "books"
    id=db.Column(db.Integer,primary_key=True,unique=True)
    name=db.Column(db.String(64),unique=True,index=True)
    author_id=db.Column(db.Integer,db.ForeignKey("authors.id"))
    pass

@app.route("/")
def index():
    authors=Author.query.all()
    return render_template("books.html",authors=authors)
    pass

if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    au1 = Author(name='A_Jalalidin')
    au2 = Author(name='A_Otkur')
    db.session.add_all([au1, au2])
    db.session.commit()
    pass
    bk1=Book(name="Ozini izdax bosugis da" , author_id=au1.id)
    bk2=Book(name="iz" , author_id=au2.id)
    bk3=Book(name="oygan gan zimin" , author_id=au2.id)
    db.session.add_all([bk1, bk2,bk3])
    db.session.commit()
    pass
    app.run()
