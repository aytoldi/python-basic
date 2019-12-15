from flask import Flask,request
app=Flask(__name__)


@app.route("/hello",methods=["get"])
def index():
    name=request.args.get("name")
    age=request.args.get("age")
    return "name=%s,age=%s" %(name,age)

if __name__ == '__main__':
    app.run()