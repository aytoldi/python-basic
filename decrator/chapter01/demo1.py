def log(func):
    def wrapper():
        print("start")
        func()
        print("end")
    return wrapper

# بىز decrotor نى ئىشلەتكەندە ئىجرا بولغان فونكىسيەگە ئۆزگەرتىش ئېلىپ بارماي ، ئەسلدىكى فونكىسيەگە يېڭى ئىقدىدار قوشالايمىز
@log
def hello():
    print("hello")

# مەسلەن hello ئىجرا بولغاندا  ، decrotor نى ئىشلتىپ hello غا ئۆزگەرتىش قوشماي ، log نىڭ ئىچدىكى نەرسىلەرنى hello غا قوشالايمىز
if __name__ == '__main__':
    hello()
