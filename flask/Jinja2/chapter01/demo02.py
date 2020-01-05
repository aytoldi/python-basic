from flask import Flask,render_template,url_for
app=Flask(__name__)

"""
    url_for 访问的url地址
"""

@app.route("/home")
def index():
    print(url_for("index")) #  يەنى route ئارقىلىق define قىلغان url ئادىرىسقا ئېرىشىش
    #/home
    return render_template("home.html")

@app.route("/mime")
def mime():
    print(url_for("mime",_external=True))# يەنى route ئارقىلىق define قىلغان پۈتۈن url ئادىرىسقا ئېرىشىش
    #http://127.0.0.1:5000/mime
    return render_template("mime.html")

if __name__ == '__main__':
    app.run()