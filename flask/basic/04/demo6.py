from flask import Flask,request
app=Flask(__name__)
@app.route("/",methods=["post"])
def upload():
    file_obj=request.files.get("pic")
    if file_obj is None:
        return "رەسىم يوللانمىدى"

    new_file=open("_pic.png","wb")
    data=file_obj.read()
    new_file.write(data)
    new_file.close()
    return "رەسىم يوللاش مۇۋەپىقيەتلىك بولدى"



if __name__ == '__main__':
    app.run();