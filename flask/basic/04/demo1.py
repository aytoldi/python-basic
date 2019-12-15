from flask import Flask,url_for,redirect
app=Flask(__name__)
#通过methods限定访问方式
@app.route("/",methods=["GET"])
def _index():
    return "index page"

@app.route("/commit", methods=["POST"])
def login():
    return {
        "success":True
    }

def login():
    # url="/" 
    url=url_for("_index") 
    return redirect(url);

if __name__ == '__main__':
    app.run();
    