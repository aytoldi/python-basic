#flask_wtf 当中引入了FlaskForm
from flask import Flask,request,render_template
app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def index():
    if request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")
        password2=request.form.get("password2")
        """
            多条件判断代码
            all函数测试迭代对象中是否所有条件都成立
            all([True,False,True]) 结果为False
            any测试是否至少有一个条件成立
            any([True,False,False]) 结果为True
            if all ([True,True,False])#都不为空时all函数返回true
        """
        #我加上了not， !True
        if not all([username,password,password2]):
            print ("value is null")
        else:
            if password!=password2:
                print ("not equal to")
            else:
                return "success"
    return render_template("demo1.html")

if __name__ == '__main__':
    app.run()

