#循环多维列表
list=[["name","lucky"],["age",18]];
"""
    ئې: item بولسا list نىڭ ئىچدىكى ھەربىر كىىچك list نى كۆرستىدۇ ، ئايرىم - ئايرىم ["age",18] ۋە ["name","lucky"]
    item[0]=["name","lucky"];
    item[1]=["age",18];
"""
for item in list:
    for i in item:
        print(i);
"""
一个序列当中包含了一个表达式的变量，它可以开始for循环。
for循环通过一个迭代变量 iterator_var 后面的序列当中去取值。
迭代变量iterator_var 取到list中的第一个值后，执行到：后面的代码块.
代码块执行完成之后，迭代变量iterator_var 去取到list的下一个值....
"""