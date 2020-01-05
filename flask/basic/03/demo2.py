from flask import Flask,render_template,redirect
from flask_wtf import FlaskForm #falskForm 扩展
from wtforms import StringField,PasswordField,SubmitField   #属性组件
from wtforms.validators import DataRequired #验证器
app=Flask(__name__)
"""
    csrf校验
    要求请求的时候cookie必须包含一个值
    要求请求体当中必须包含一个值
"""
app.config["SECRET_KEY"]="helloPython"
class LoginForm(FlaskForm):
    """自定义的注册表单模型类"""
    #   <input id="user_name" name="user_name" type="text" value=""/>
    user_name = StringField(label=u"用户名",validators=[DataRequired(u"用户名不能为空")])
    #   <input id="user_password" name="user_password" type="text" value=""/>
    user_password=PasswordField(label=u"密码",validators=[DataRequired(u"密码不能为空")])
    #   <input id="user_submit" name="user_submit" type="submit" value="user_submit"/>
    user_submit=SubmitField(label=u"提交")

@app.route("/login",methods=["GET","POST"])
def login():
    #创建表单对象
    form=LoginForm()
    """
        判断form当中的数据是否符合表单提交
        如果符合返回True，否则返回False
    """
    if form.validate_on_submit():#返回True还是False
        #提取数据
        name=form.user_name.data
        password=form.user_password.data
        return redirect("index")

    return render_template("home.html",form=form)

@app.route("/index")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()

#https://segmentfault.com/a/1190000015228524