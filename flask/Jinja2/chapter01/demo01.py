from flask import Flask,render_template_string
app=Flask(__name__)

"""
    render_template()            html自动转移,渲染模板文件
    render_template_string()     字符串自动转移，渲染字符串    
    {% autoescape %}             手动设置是否转义
"""

@app.route("/")
def index():
    html="<ul><li>hello</li><li>world</li></ul>"
    return render_template_string(html)

if __name__ == '__main__':
    app.run()