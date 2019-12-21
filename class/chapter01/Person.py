class Person:

    # ئاسىتى سىزىق init بولسا ئۇ بىر class نىڭ constructor سى
    # تىرناق ئىچدىكى self بولسا java دىكى this بىلەن ئوخشاش ، يەنى create قىلغان Object نى كۆرسىتدۇ
    def __init__(self,name):
        self.__name=name
        pass

    def show(self):
        return self.__name
        pass #不做任何事情，只起到占位的作用  ھىچقانداق رولى يوق ، ئەمما كود بۆلىكى قۇرۇق بولمىسا قىزىل ئاگاھلاندۇرۇش چىقۋالدۇ

obj=Person("bell")
getName=obj.show()
print(getName)







