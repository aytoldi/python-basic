from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("demo1.html",name="hello")

if __name__ == '__main__':
    app.run()