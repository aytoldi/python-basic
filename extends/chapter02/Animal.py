# -*- coding:utf-8 -*-
class Animal():
    def __init__(self, name):
        self.name = name

    def saySomething(self):
        print("I am " + self.name)


class Dog(Animal):
    def __init__(self, name,color):
        super().__init__(name)
        self.color=color

    def saySomething(self):
        print("I am " + self.name + ", and I can bark "+self.color)

    # 3.在类定义中调用本类的父类方法，可以直接 super().parent_method(arg)  【个人推崇这种写法】
    def animal_say(self):
        #  方式 [推荐]
        super().saySomething()

if __name__ == "__main__":
    dog = Dog("Blake","white")
    dog.saySomething()
    dog.animal_say()
    # 子类对象调用被覆盖的父类方法
    # super(Dog, dog).saySomething()