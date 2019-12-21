class HouseItem:
    def __init__(self,name,area):
        self.name=name
        self.area=area
        pass

    def __str__(self):
        return "[%s] 占地 .%2f " %(self.name,self.area)
        pass


class House:
    def __init__(self,desc,area):
        self.desc=desc
        self.area=area
        self.freeArea=area
        self.list=[]
        pass

    def __str__(self):
        return ("新增房子是 %s , 总面积 %.2f , 剩余面积 %.2f"
                %(self.desc,
                  self.area,
                  self.freeArea,
                  self.list)
                )
        pass

    def addHouseItem(self,item):
        print("要添加%s" %(item))
        """
        ئۆي ئىچىگە ئۆي جازىلىرنى تىزىشتىن ئىلگىرى ، ئۆينىڭ ئىچىدىكى قۇرۇق ئۇرۇن بىلەن ئۆي جاھازىسى ئىگەلليدىغان ئۇرۇننى سېلىشتۇرۇش ،
        ئەگەر ئۆي ئىچىدىكى بوش ئۇرۇن ، ئۆي جاھازىسى ئىگەللەيدىغان ئۇرۇندىن چوڭ بولسا ، ئۆي جاھازىسنى قۇيۇشقا بولىدۇ.
        ئۇنداق بولمىسا ، يەنى ئۆي ئچىدىكى بوش ئۇرۇن  ، ئۆي جاھازىسى ئىگەللەيدىغان ئۇرۇندىن كىچىك بولسا ئۆي جاھازىسنى قۇيۇشقا بولمايدۇ.
        """
        if self.freeArea>item.area:
            print("ئۆي ئىچىگە [%s] قۇيۇلدى"%(item.name))
            self.list.append(item.name)
            """
             ئۆي جاھازىسى ئۆي ئىچىگە قۇيۇلۇپ بولغاندىن كىيىن ، ئۆينىڭ نەرسە قويدىغان ئۇرۇن كىچىكلەيدۇ
             بۇنى ھىسابلىماقچى بولساق ، ئۆينىڭ ئەسلدىكى نەرسە قويدىغان بوش ئۇرۇندىن ئېلۋېتىمىز ئۆي جاھازىسى ئىگەلللىگەن ئۇرۇننى
            """
            self.freeArea=self.freeArea-item.area
            pass

        if self.freeArea<item.area:
            print("ئۆي ئىچى تۇشۇپ كەتتى [%s] پاتمايدۇ ، لازىم ئەمەس"%(item.area))
            pass
    pass

    def readList(self):
        return self.list
        pass


bed = HouseItem("bea",4.3)
bookself = HouseItem("bookself",2.1)
coathanger= HouseItem("coathanger",2.3)

myHouse = House("两室一厅",60.0)
myHouse.addHouseItem(bed)
myHouse.addHouseItem(bookself)
myHouse.addHouseItem(coathanger)
list=myHouse.readList()
for i in list: # ئۆي ئىچگە قۇيۇلغان ئۆي جاھازلىرىنىڭ ئىسمنى چىقرىش
    print(i)