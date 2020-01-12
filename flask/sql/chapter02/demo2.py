from flask import Flask,render_template,request,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import fields,validators

import sys
import importlib
importlib.reload(sys)

app.config['SECRET_KEY'] = 'A RANDOM STRING'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1:3303/book?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True
db=SQLAlchemy(app)

class Authors(db.Model):
    __tablename__="author"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(64),index=True,unique=True)
    myBook=db.relationship("Books",backref="book")
    pass

class Books(db.Model):
    __tablename__="book"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(64),index=True)
    author_id=db.Column(db.Integer,db.ForeignKey("author.id"))
    pass

class BookManager(FlaskForm):
    autName=fields.StringField(label="作者",validators=[validators.DataRequired(message="作者不能为空")])
    book=fields.StringField(label="书",validators=[validators.DataRequired(message="书不能为空")])
    submit=fields.SubmitField("提交")
    pass

@app.route("/",methods=["GET","POST"])
def index():
    form=BookManager()
    # 1.ئالدى بەك form دىكى ئۇچۇرلارنى يوللاش
    if form.validate_on_submit():
        #2.ئالدى بەت form دىن ئەۋەتكەن form دىكى سانلىق مىقدارلاغا ئېرىشىش
        getAuthorValue=form.data["autName"];
        #3.ساندانغا ئاپتۇرنىڭ ئۇچۇرنى قوشۇشتىن ئاۋال ، ئاپتۇرنى سانداننىڭ ئىچدىن تەكشۈرىمەن ، ئەگەر ئاپتۇر ئۇچۇرى بار بولسا Object قايتىدۇ ،  table دىكى بىرىنچى قۇر ئۇچۇرغا ئېلىش
        author_obj=Authors.query.filter_by(name=getAuthorValue).first()
        #5.ئەگەر ئاپتۇرنىڭ ئۇچۇرى سانداندا ساقلانغان بولسا
        if author_obj:
            getBookValue = form.data["book"];
            #سانداندا نۆۋەتتكى كىتاب ساقلانغان ، table دىكى بىرىنچى قۇر ئۇچۇرغا ئېلىش
            book_obj=Books.query.filter_by(name=getBookValue).first()
            # 7.كىتابنىڭ سانداندا ساقلانغان ساقلانمىغانلىقغا ھۈكۈم قىلىش
            if book_obj: # كىتاب ساقلانغان بولسا
                flash("重复数据，book已经存在")
            else:
                #8.نۆۋەتتىكى كىتاب سانداندا يوق ، كىتاب قوشسا بولىدۇ
                #ئەگەر ساندانغا كىتاب قۇشۇشتا مەسىلە چىقسا قانداق قىلىش كېرەك ؟
                try:
                    new_book=Books(name=getBookValue,author_id=author_obj.id)
                    db.session.add(new_book)
                    db.session.commit()
                except Exception as e:
                    flash("数据库添加失败")
                    db.session.rollback()
        #6.ئاپتۇرنىڭ ئۇچۇرىنى سانداندىن تاپامىغان بولسا ، ئاپتۇرنىڭ ئۇچۇرى ۋە كىتاب ئۇچۇرىنى ساندانغا قوشسۇن
        else:
            try:
                getAuthorValue = form.data["autName"];
                new_author = Authors(name=getAuthorValue)
                db.session.add(new_author)
                db.session.commit()
                pass
                getBookValue = form.data["book"];
                new_book = Books(name=getBookValue, author_id=new_author.id)
                db.session.add(new_book)
                db.session.commit()
                pass
            except Exception as e:
                flash("数据库添加失败")
                db.session.rollback()
                pass
    else:
       if request.method=="post":
            flash("参数不全")
    data=Authors.query.all()
    return  render_template("newBook.html",form=form,data=data)

@app.route('/delete_book/<book_id>')
def delete_book(book_id):
    # ساندانغا ئۈچۈرمەكچى بولغان كىتابنىڭ id سىنى ئەۋەتىمەن ، ساندان ئىزدەپ True قايتۇرسا ،  مەن بىر Object قا ئېرىشمەن
    book_obj=Books.query.get(book_id)
    if book_obj:
        try:
            # سانداندىن id ئارقىلىق ئىزدەپ تاپقان كىتابنىڭ بارلىق ئۇچۇرىنى ئۈچۈرۋېتىش
            db.session.delete(book_obj)
            db.session.commit()
        except  Exception as e:
            flash("删除失败")
            db.session.rollback()
    else:
        print("书籍找不到")
        pass
    return redirect(url_for("index"))

@app.route('/delete_author/<author_id>')
def delete_author(author_id):
    # ساندانغا ئۈچۈرمەكچى بولغان يازغۇچنىڭ id سىنى ئەۋەتىمەن ،  ساندان ئىزدەپ True قايتۇرسا  ،  مەن بىر Object قا ئېرىشمەن
    author=Authors.query.get(author_id)
    # يازغۇچنى ئۈچۈرگەندە ئاۋال ، يازغۇچنىڭ كىتابلىرنى ئۈچۈرىمەن ، ئاندىن يازغۇچنىڭ ئۆزىنى ئۈچۈىمەن
    if author:
        try:
            """
                كىتابنى ئۈچۈرۈش
            كىتاب  Books نىڭ ئىچدىكى author_id نىڭ قىممىتى author.id غا تەڭ بولغاندىكى كىتابلارنىڭ ھەممىنى سانداندىن ئۈچۈرۈش  
            """
            Books.query.filter_by(author_id=author.id).delete()
            #ئاندىن يازغۇچنى ئۈچۈرۈش 2.
            db.session.delete(author)
            db.session.commit()
        except  Exception as e:
            flash("删除失败")
            db.session.rollback()
    else:
        print("书籍找不到")
        pass
    return redirect(url_for("index"))


if __name__ == '__main__':
    db.drop_all()
    db.create_all()

    au1=Authors(name="Loiane Groner")
    au2=Authors(name="Jason Strimpel")
    au3=Authors(name="Kyle Simpson")
    db.session.add_all([au1,au2,au3])
    db.session.commit()

    bk1=Books(name="学习JavaScript数据结构与算法",author_id=au1.id)
    bk2=Books(name="同构JavaScript应用开发",author_id=au2.id)
    bk3=Books(name="你不知道的JavaScript",author_id=au3.id)
    db.session.add_all([bk1,bk2,bk3])
    db.session.commit()
    app.run(debug=True)