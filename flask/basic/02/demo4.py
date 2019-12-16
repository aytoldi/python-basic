from flask import Flask,render_template
#https://blog.csdn.net/troysps/article/details/80466916
app=Flask(__name__)
@app.route("/")
def index():
    return render_template("demo4.html",my_list=[1,2,3,4,5])

@app.template_filter("li")
def device(el):
    return el[::3]
if __name__ == '__main__':
    app.run()