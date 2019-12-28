from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

class Config:
	app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1:3306/test'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config.from_object(Config)
db = SQLAlchemy(app)

class Role(db.Model):
	__tablename__="tb_role"
	id=db.Column(db.Integer,primary_key=True)#角色id
	name=db.Column(db.String(64),unique=True)#管理员还是普通用户
	"""
		مۇشۇ Role دىگەن Model نى باغلاپ ئىشلەتكەن Model نى relationshio قا ئەۋەتىپ بىرىپ.
		 مەسلەن :  Users دىگەن Model نى relashionship قا ئەۋەتتۇق ، ئاندىنRole دىگەن Model دا تۇرۇپ  Users نىڭ ئىچىدىكى خاسلىقلارغا ئېرىشىش 
		 يەنى user ئارقىلىق Role دىگەن Model نى باغلاپ ئىشلەتكەن ئەزانىڭ ئۇچۇرلىرنى تەكشۈرۈپ چىقالايمىز ، ئاندىن ئەزانىڭ role سىنى بېكتەلەيمىز .
		 
		 بۇ يەردە مەن Users دىگەن Model غا role دەپ بىر خاسلىق قوشتۇم ، backref بولسا تەتۈرىگە چىكنىش دىگەن مەنىدە. 
		 بۇ يەردە" backref="ref" نى ئىشلتىشمىزدىكى مەقسەت user.role بىلەن قىممەت ئىرشكەندە ،
		  Users دىگەن Model غا باغلانغان Role دىگەن Model نىڭ ئىچىدىكى باشقا نەرسلەرنىمۇ تەكشۈرۈلەيمىز 
	"""
	user=db.relationship("Users",backref="role")

class Users(db.Model):
	__tablename__="users"
	"""
	يېزىلغان Model نىڭ خاسلىقلىرنى ئېنىقلاش .
	مەسلەن : ئەزانىڭ id خاسلىقىنىڭ تىپى integer يەنى سان ، primary_key بولسا ئاساسىي ھالقىنى بىلدۈردۇ ، unique بولسا تەكرارلانمايدۇ دىگەننى بىلدۈردۇ.
	ئەزانىڭ name خاسلىقنىڭ تىپى بولسا String ھەرىپ بەلگە تىپى ، ئۇزۇنلۇقى 64 ، unique ئەزانىڭ ئىسمى تەكرارلانمايدۇ ، index بولسا ئىزدەش ئېلىپ بارغاندا index دىن پايدىلىندۇ.
	ئەزانىڭ password خاسلىقنىڭ تىپى بولسا Interger
	"""
	id=db.Column(db.Integer,primary_key=True,unique=True)
	name=db.Column(db.String(64),unique=True,index=True)
	password=db.Column(db.Integer)
	"""
		 ئەگەر ئەزا ئۆز ئىچىگە ئالغان خاسلىقلار باشقا table بىلەن باغلنىشلىق مۇناسىۋەتتە بۇلۇپ قالسا ، Column غا ئاۋال ئەزانىڭ خاسلىقنى يازىمىز .
		 ئاندىن ForeignKey نىڭ ئىچىگە مۇشۇ Model بىلەن باغلنىشلىق مۇناسۋەتتە بولغان جەدىۋەلدىكى خاسلىق ئۇچۇرلىرنى يازىمىز . 
	"""
	role_id=db.Column(db.Integer,db.ForeignKey("tb_role.id"))
	pass
if __name__ == '__main__':
	""" سانداندىكى بارلىق ئۇچۇرلارنى ئۈچۈرۈش """
	db.drop_all()
	"""
	يۇقىردىكى Model class غا يېزىلغان بارلىق table نى Mysql ساندانغا قۇرۇپ چىقىش 
	"""
	db.create_all()