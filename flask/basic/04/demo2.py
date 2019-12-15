from flask import Flask
app=Flask(__name__)

#   http://127.0.0.1:5000/goods/2
@app.route("/goods/<int:goods_id>")
def goods_detail(goods_id):
    return "%s" % goods_id

@app.route("/user/<id>")
def user_detail(id):
    return "%s" % id

if __name__ == '__main__':
    app.run()