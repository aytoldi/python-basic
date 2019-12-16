from flask import Flask,request,render_template

app=Flask(__name__)

@app.route("/xss",methods=["GET","POST"])
def index():
    text=""
    if request.method=="POST":
        text=request.form.get("content")

    return render_template("demo3.html",text=text)

if __name__ == '__main__':
    app.run()