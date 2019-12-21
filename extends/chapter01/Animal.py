class Animal:
    def __init__(self,name,meal):
        self.name=name
        self.meal=meal
        pass

    def eat(self):
        print("%s 喜欢吃 %s" %(self.name,self.meal))
        pass

    def run(self):
        print("%s 喜欢跑步" %self.name)
    pass
# بالا تۈر Dog ، دادا تۈر Animal نى extends قىلدى
# بالا تۈر دادا تۈرنىڭ بارلىق خاسلىق ۋە method لىرنى ئىشلىتەلەيدۇ ، بالا تۈر ئۆزىگە خاسلىق ۋە method قوشالايدۇ


class Dog(Animal):
    def __init__(self,name,meal,color):
         # بالا تۈر دادا تۈردىكى خاسلىقلارنى ئىشلەتكەندە super().__init__(all) تىرناق ئىچىگە دادا تۈردىكى بارلىق خاسلىقلارنى يېزىشى كېرەك
        super().__init__(name,meal)
        self.color = color
        pass

    def greet(self):
        print("my name %s , color is %s" %(self.name,self.color))
        pass

    """"
    بالا تۈردە super(). نى ئىشلتىپ ,  ئەسلىدىكى دادا تۈردە يېزىلغان methods لارنى call method قىلالايمىز 
     بالا يۈردە دادا تۈردىكى methods لارنى ئىشلەتمەكچى بولساق ،
      بالا تۈرنىڭ ئىچدە ئىشلتىدىغان method نى قايتىدىن تەكرار يازىمىز ، method نىڭ ئىچگە super().method نى يازىمىز
     """

    def eat(self):
        super().eat()
        pass

    def run(self):
        super().run()
        pass
    pass


if __name__ == '__main__':
    dog = Dog("balabala", "白菜","white")
    dog.greet()
    dog.eat()
    dog.run()

