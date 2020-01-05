from flask import Flask,render_template
app = Flask(__name__)

"""
	模版继承和block的目的就是为了减少前端代码量

	block语法：
	一般在父模版中，定义一些公共的代码。子模版可能要根据具体的需求实现不同的代码。

	这时候父模版就应该提供一个接口，让父模版来实现。从而实现具体业务需求的功能。

	在父模版中：

	使用父模板块 (Block)的内容
	如果子模板想使用父模板中的块里的内容，请使用{{ super() }}。请看下面例子

	{% extends 'base.html' %}
	{% block 块名 %}
	    块内容
	{% endblock (块名)%}


"""

@app.route('/')
def index():
	return render_template("index.html")

if __name__=='__main__':
	app.run(debug=True)