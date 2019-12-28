from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

class Config:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1:3306/test'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config.from_object(Config)
db = SQLAlchemy(app)

class Role(db.Model):
    __tablename__ = "tb_role"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    """
        مودىل Role ئىچىدىكى باشقا جەدىۋەلدىن باغلانغان Users دەپ ئېنىقلىما بىرىلگەن Model نىڭ ئۇچۇرلىر  غا ئېرىشىش
    """
    user = db.relationship("Users", backref="role")

class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.Integer)
    role_id = db.Column(db.Integer, db.ForeignKey("tb_role.id"))

if __name__ == '__main__':
    db.drop_all()
    db.create_all()

    #保存数据

    role1=Role(name="admin")#创建对象
    db.session.add(role1) #session记录对象
    db.session.commit()#提交数据库中

    role2=Role(name="stuff")
    db.session.add(role2)
    db.session.commit()

    user1=Users(name="tahirjan",password="123",role_id=role1.id)
    user2=Users(name="rizwangul",password="123",role_id=role1.id)
    user3=Users(name="raziya",password="1234",role_id=role2.id)
    user4=Users(name="gulzira",password="123456",role_id=role2.id)

    #一次提交多条记录
    db.session.add_all([user1,user2,user3,user4])
    db.session.commit()