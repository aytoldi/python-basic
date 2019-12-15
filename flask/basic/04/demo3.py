from flask import Flask,request

app=Flask(__name__)
@app.route("/hello",methods=["get","post"])
def index():
    """
        request 中包含了前端发过来的所有请求参数
        request.form可以直接提取请求体中的表单格式的数据，是一个字典的对象
        ئەگەردە request ئۇچۇرنى get شەكلىدە يوللىسا ، ناۋادا مۇلازىمتىرغا يوللىغان مەلۇم بىر ئۇچۇر قۇرۇق ئەۋەتىلىپ قالسا ، بىزگە none قايتىدۇ
        قايتىپ كەلگەن none نى باشقا ئۇچۇرغا ئۆزگەرتمەكچى بولساق
        age=request.form.get("age","0"); شەكلىدە كېلىپ قالسا get  دىن كەلگەن ئۇچۇر form  ئەگەر
        مەسلەن requst دىن كەلگەن get ئۇچۇر  مەسلەن age قۇرۇق بۇپ قالسا مەن 0 دەپ قىممەت چىقسۇن دىدىم
    """
    username=request.form.get("username") # ئالدى بەت form دىن كەلگەن ئۇچۇر request.form نىڭ ئىچىدە بولىدۇ
    age=request.form.get("age")
    return  "hello name=%s,age=%s" %(username,age)
if __name__ == '__main__':
    app.run()