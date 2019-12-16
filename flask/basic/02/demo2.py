from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def index():
    obj={
        "name":"flask",
        "version":{
            "one":1.1,
            "two":1.5
        },
        "functionDevice":["orm","template","form"]
    }
    # ** 扩展运算符 ， نىڭ تىرناق نى ئۈچۈرۈپ ، ئېلمىنتلارنى كېڭەيدىغان ھالەتكە ئۆزگەرتىش object
    return render_template("demo2.html",**obj)

if __name__ == '__main__':
    app.run()
