from flask import Flask
app=Flask(__name__)

class Config(object):
   Debug=True
   school="python..."

app.config.from_object(Config)

@app.route("/")
def index():
    # پۈتۈن دائىردىكى setting نىڭ ئىچدىكى ئۇچۇرنى ئۇقۇپ ئېلىش
    name=app.config.get("school")
    print(name)
    return "hello ..."

if __name__ == '__main__':
    app.run()