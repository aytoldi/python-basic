class Person:
    """
        A.
        قەدىردان يۈگۈرەشنى ياخشى كۆرىدۇ ، بەدەن ئېغىرلىقى 53.0kg .
         قەدىردان ھەر قېتىم يۈگۈرگەندە 0.5kg ئۇرۇقلايدۇ , ھەرقېتىم بىر نەرسە يىسە 1.0kg سەمرەيدۇ

        B.
         تەھلىل : بىر ياش يىگىت بار ئىكەن ئىسمى قەدىردان ئىكەن ، ئېغىرلىقى 53.0 كىلوگرام ئىكەن .
         يۈگرەشنى ۋە نەرسە يىيشنى ياخشى كۆردىكەن
        C.
        بۇ ئادەمنىڭ ئىسىم ۋە بەدەن ئېغىرلىقدىن ئىبارەت ئىككى خىل خاسلىقى بېرىلپتۇ .
        بىر نەرسە يېيىش ۋە يۈگرەشنى ياخشى كۆردىغانلىقتىن ئىبارەت ئىككى ھەركەت ئالاھىدلىكى بار ئىكەن

        D.
        تۈردىكى خاسلىقلارنى ۋە ھەركەت method نى ئىپادىلەپ چىقىش
        name , weight
        run() , eat()
    """

    # قەدىرداننىڭ ئىسىم ۋە بەدەن ئېغىلرلىقدىن ئىبارەت ئىككى خىل خاسلىقنى دەسلەپپلەشتۈرۈش ، يەنى init قىلىش
    def __init__(self, name, weight):
        # بۇيەردىكى self.name ۋە self.weight بولسا مۇشۇ Person تۈرنىڭ خاسلىقى ھىسابلىندۇ
        self.name = name
        self.weight = weight
        pass

    def __str__(self):
        # 小数点后面只保留两位
        return "my name %s , my weight %.2f kg" %(self.name, self.weight)
        pass

    # يۈگۈرەش ، يەنى بەدەن چېنىقتۇردىغان بىر method بار
    def run(self):
        print("%s 爱跑步, 跑步锻炼身体" %(self.name))
        self.weight=self.weight-0.5
        pass

    def eat(self):
        print("%s 爱吃东西, 吃完这顿再减肥吧" %(self.name))
        self.weight=self.weight+1.0
        pass

Qdadirdan = Person("tahirjan",53.0)
Qdadirdan.run()
Qdadirdan.eat()
print(Qdadirdan)

