from flask import Flask,request
app=Flask(__name__)

@app.route("/hello",methods=["get","post"])
def index():
    if request.method=="get":
        return  "aa"
    if request.method=="post":
        return "bb"
if __name__ == '__main__':
    app.run()