from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 设置连接数据库的URL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1:3303/world'

# 设置每次请求结束后会自动提交数据库的改动
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    """
        يۇقىردا ModelClass Role غا id , name دەپ خاسلىق قوشتۇق .
        قۇشۇلغان name, id قاتارلىق خاسلىقلار ModelClass Role غا تەۋە .
        تۆۋەندە بىز ModelClass Role غا تەۋە بولغان يەنە بىر user دەپ خاسلىق قوشماقچى .
        بۇ خاسلىق ئارقىلىق ModelClass Role غا باغلانغان ModelClass User نىڭ ئۇچۇرىنى تەكشۈرگىلى بولىدۇ .
    """
    user = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True)
    pswd = db.Column(db.String(64))
    """
        ئەزانىڭ ھۇقۇقىنى بېكتىدىغان خاسلىق ، يەنى ئەزا ئادەتتىكى ئەزااغا تەۋەمۇ ، ئالى ئەزاغا تەۋەمۇ ؟
    """
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return 'User:%s' % self.name


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    ro1 = Role(name='admin')
    ro2 = Role(name='user')
    db.session.add_all([ro1, ro2])
    db.session.commit()