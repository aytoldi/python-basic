from flask import Flask
app=Flask(__name__)
@app.route("/")
def index():
    return "hello"
#运行主模块系统
if __name__ == '__main__':
    app.run()
