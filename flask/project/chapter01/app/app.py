# -*- coding: utf-8 -*-
import importlib
import sys

from flask import Flask, render_template,flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import fields
importlib.reload(sys)

#forms
class ProductAddForm(FlaskForm):
    # 商品标题
    title = fields.StringField(label="商品标题",render_kw={"class":"form-control","placeholder":""})
    # 描述
    content = fields.TextAreaField(label="商品描述",render_kw={"class":"form-control","placeholder":""})
    # 商品推荐语
    recommend = fields.StringField(label="商品推荐语",render_kw={"class":"form-control","placeholder":""})
    # 类型
    types = fields.SelectField(label="商品类型",render_kw={"class":"form-control","placeholder":""},choices=[(1, '销售中'), (2, '已售完'), (3, '未开始')])
    # 价格
    price = fields.IntegerField(label="商品价格",render_kw={"class":"form-control","placeholder":""})
    # 原价
    origin_price = fields.FloatField(label="原价",render_kw={"class":"form-control","placeholder":""})
    # 商品图片
    img = fields.FileField(label="商品图片",render_kw={"class":"form-control","placeholder":""})
    # 商品链接
    link = fields.StringField(label="商品链接",render_kw={"class":"form-control","placeholder":""})
    # 商品状态
    status = fields.SelectField(label="商品状态",render_kw={"class":"form-control","placeholder":""},choices=[(1, '销售中'), (2, '已售完'), (3, '未开始')])
    # 库存
    sku_count = fields.IntegerField(label="商品库存",render_kw={"class":"form-control","placeholder":""})
    # 剩余库存
    remain_count = fields.IntegerField(label="商品剩余库存",render_kw={"class":"form-control","placeholder":""})
    # 访问次数 visits
    view_count = fields.IntegerField(label="访问次数",render_kw={"class":"form-control","placeholder":""})
    # 评分
    score = fields.IntegerField(label="评分",render_kw={"class":"form-control","placeholder":""})
    # 逻辑删除
    is_valid =fields.BooleanField(label="逻辑删除",render_kw={"class":"form-control","placeholder":""})
    # 排序
    reorder = fields.IntegerField(label="排序",render_kw={"class":"form-control","placeholder":""})
pass

"""
app = Flask(
    __name__,
    template_folder='.',  # 表示在当前目录 (myproject/A/) 寻找模板文件
    static_folder='../',  # 表示为上级目录 (myproject/) 开通虚拟资源入口
    static_url_path='',  # 这是路径前缀, 个人认为非常蛋疼的设计之一, 建议传空字符串, 可以避免很多麻烦
)

"""

app=Flask(__name__)
app.config['SECRET_KEY'] = 'A RANDOM STRING'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1:3303/book?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True
db=SQLAlchemy(app)

#class


#标签
class ProductTag(db.Model):
    #商品标签
    __tablename__="product_tag"
    id=db.Column(db.Integer,primary_key=True)
    #标签名称
    name=db.Column(db.String(64),nullable=False)
    #标签编码
    code=db.Column(db.String(128))
    #标签描述
    desc=db.Column(db.String(128))
    #逻辑删除
    is_valid=db.Column(db.Boolean,default=True)
    #排序
    reorder=db.Column(db.Integer,default=0)
    #创建时间
    create_date=db.Column(db.DateTime)
    #最后修改时间
    update_date=db.Column(db.DateTime)
    #关联商品
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"))
pass

#分类
class ProductClass(db.Model):
    #商品分类
    __tablename__ = "product_class"
    id = db.Column(db.Integer, primary_key=True)
    # 分类名称
    name = db.Column(db.String(64), nullable=False)
    # 分类编码
    code = db.Column(db.String(128))
    # 分类描述
    desc = db.Column(db.String(128))
    # 逻辑删除
    is_valid = db.Column(db.Boolean, default=True)
    # 排序
    reorder = db.Column(db.Integer, default=0)
    # 创建时间
    create_date = db.Column(db.DateTime)
    # 最后修改时间
    update_date = db.Column(db.DateTime)
    #关联商品
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"))
pass

#商品
class Product(db.Model):
    #商品
    __tablename__="product"
    #商品id
    id=db.Column(db.Integer,primary_key=True)
    #商品名称
    name=db.Column(db.String(64),nullable=False)
    #标题
    title = db.Column(db.String(128), nullable=False)
    #描述
    content = db.Column(db.Text, nullable=False)
    #商品推荐语
    recommend  = db.Column(db.String(64))
    #类型
    types = db.Column(db.Enum("实物商品","虚拟商品"))
    #价格
    price = db.Column(db.Integer, nullable=False)
    #原价
    origin_price = db.Column(db.Float)
    #商品图片
    img = db.Column(db.String(256), nullable=False)
    #商品链接
    link = db.Column(db.String(256))
    #商品状态
    status = db.Column(db.Enum("销售中","已售完"))
    #库存
    sku_count = db.Column(db.Integer, default=0)
    #剩余库存
    remain_count=db.Column(db.Integer,default=0)
    # 访问次数 visits
    view_count = db.Column(db.String(64))
    #评分
    score = db.Column(db.Integer, default=10)
    # 逻辑删除
    is_valid = db.Column(db.Boolean, default=True)
    # 排序
    reorder = db.Column(db.Integer, default=0)
    #创建时间
    create_date=db.Column(db.DateTime)
    #最够修改时间
    update_date=db.Column(db.DateTime)
    # 商品跟分类之间的关系,商品跟标签之间的关系
    product_tag_id=db.relationship("ProductTag",backref="tags")
    product_class_id=db.relationship("ProductClass",backref="classes")
pass

"""
    url_for()函数是用于构建指定函数的URL。 
    https://www.cnblogs.com/guyuyun/p/9942859.html
    https://www.cnblogs.com/wuheng-123/p/9663294.html
"""

@app.route("/")
def index():
    return render_template("mall/index.html")
pass

@app.route("/product/add",methods=['GET','POST'])
def product_add():
    form=ProductAddForm()
    if form.validate_on_submit():
        #把数据保存数据库

        #消息提示
        flash("新增成功","success")
        pass
    else:
        flash("请修改页面中的错误，然后提交","warning")
        pass

    return render_template("mall/product_add.html",form=form)
pass

if __name__ == '__main__':
    app.run()