# -*- coding: utf-8 -*-
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm # extends Flask  form
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired
import sys
import importlib
importlib.reload(sys)

app=Flask(__name__)
app.config['SECRET_KEY'] = 'A RANDOM STRING'

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
    يازغۇچنىڭ يازغان كىتابلىرى قايسىلار ؟
    يازغۇچى Auther دىگەن ModelClass دا ھىچقانداق كىتابنىڭ ئۇچۇرى يوق ، پەقەت يازغۇچنىڭ ئىسمى ، يازغۇچنىڭ ساندان خاتىرلىگەن id قاتارلىق ئۇچۇرلىرى بار.
    كىتابنىڭ ئۇچۇرلىرى books دىگەن جەدىۋەلدە ساقلانغان .
    
    
    قانداق قىلغاندا يازغۇچى يازغان كىتابلارنىڭ ئۇچۇرىنى تاپالايمەن ؟
    مەن ئاۋال Book دەپ ModelClass دىن بىرنى قۇراي .
    كىتاب دىگەندە كىتابنىڭ ئىسمى بولىدۇ ، ئاپتۇرى بولىدۇ .
    مەن ئاۋال جەدىۋەلدىن بىرنى قۇراي ، جەدىۋەلگە books دەپ نام بىرەي .
    ئاندىن جەدىۋەلگە كىرگۈزدىغان ئۇچۇرلارنىڭ Model نى ئېنىقلاي .
    كىتابنىڭ ئىسمىنى name دەپ ئېنىقلاي .
    
    كىتاب ئاپتۇرىنىڭ ئۇچۇرلىرى باشقا بىر سانداندا ساقلانغا ، كىتاب ئاپتۇرنى ئېنىقلاش ئۈچۈن قانداق قىلىش كىرەك ؟
    ئاپتۇرلارنىڭ سانداندا ئۇچۇرى خاتىرلەنگەندە ئۇلارنىڭ ئۇچۇرلىرغا id ئېنىقلانغان بولىدۇ .
    بىز مۇشۇ سانداندا خاتىرلەنگەن id ئارقىلىق ئاپتۇرنىڭ باشقا ئۇچۇرلىرنمۇ ئالالايمىز ، مەسلەن ئىسمى ، يېشى ، كەسپى ، ئوقۇغان مەكتىپى دىگەندەك .
    ئەمدى Book دىگەن ModelClass نىڭ ئىچدە ئاپتۇرنىڭ ئۇچۇرلىرنى ئېلىش ئۈچۈن ، ForeignKey ئارقىلىق سىرىتتىن بىر باغ باغلايمەن .
    يەنى Author دىگەن ModelClass نىڭ ئىچىدە قۇرغان authors دىگەن جەدىۋەلنى باغ قىلىپ باغلايمەن .
    باغلىماقچى بولغان باغدىكى خاسلىقنى ForeignKey غا ئەۋەتىپ بېرىمەن .
    ئاندىن Book دىگەن ModelClass نى قۇرۇپ ،  قىممەت بەرگەندە author_id غا يازغۇچنىڭ Author دىگەن ModelClass ئوبىكتىغا خاتىرلەنگەن id ئېلىپ بېرىمەن.
    ھازىر Book دىگەن ModelClass  دا يازغۇچنىڭ ئۇچۇرىنى ئالالىغان بولدۇم .
    
    ئەمدى Author دىگەن ModelClass دا قانداق قىلىپ Book دىگەن ModelClass نىڭ ئۇچۇرىنى تەكشۈرەلەيمەن ؟
    بۇنى ھەل قىلىش ئۈچۈن relationship ئارقىلىق ئىككى ModelClass ئارىسدا بىر باغلىنىش قۇرىمەن ، يەنى Book دىگەن ModelClass  نىڭ باغلايدىغان باغنى قۇرۋالمەن .
     ئاندىن كىيىن relationship قا يەنە بىر پارامتىر قوشىمەن ، backref دەپ ، بۇنىڭ بىلەن Book غا بىر خاسلىق قوشىلدۇ ، بۇ ئارقىلىق مۇشۇ ئاپتۇرنىڭ Book دىكى كىتاب ئۇچۇرلىرنى تەكشۈرگىلى بولىدۇ . 
    
"""
class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    books=db.relationship("Book",backref="book")
    pass

class Book(db.Model):
    __tablename__ = "books"
    id=db.Column(db.Integer,primary_key=True,unique=True)
    name=db.Column(db.String(64),unique=True,index=True)
    author_id=db.Column(db.Integer,db.ForeignKey("authors.id"))
    pass

# 定义一个表单类
class AuthoForm(FlaskForm):
    #定义表单类使用的属性
    name=StringField("作者",validators=[DataRequired()])
    book=StringField("书籍",validators=[DataRequired()])
    submit=SubmitField("提交")
    # يۇقىردىكى خاسلىقلاردىكى قىممەتلەر html بەتتە 解释 بولىدۇ
    pass

@app.route("/",methods=["GET","POST"])
def index():
    authors=Author.query.all()
    # 创建一个Form 类的实例对象
    aut_form=AuthoForm()
    return render_template("books.html",authors=authors,form=aut_form)
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
