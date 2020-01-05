from flask import Flask,render_template
app=Flask(__name__)

@app.route("/home")
def home():
    list=["javascript","nodejs","reactJs"]
    return render_template("home.html",list=list)

@app.route("/mime")
def mime():
    lang=[{"name":"java"},{"name":"python"},{"name":"rust"}]
    return render_template("mime.html",lang=lang)

if __name__ == '__main__':
    app.run()