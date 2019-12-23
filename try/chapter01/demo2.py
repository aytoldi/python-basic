def test_div(num1,num2):
    return num1/num2
    pass

if __name__ == '__main__':
    try:
        val=test_div(5,0)
        print(val)
        pass
    except  TypeError:# مەسلەن : string تىپدىكى ھەرىپ ياكى سان كىرگۈزۈپ قالسا "5" || "hello"
        print("كىرگۈزگىنڭىز خاتا بۇپ قالدى ، سان كىرگۈزۈڭ")
        pass
    except  ZeroDivisionError:
        print("كىرگۈزگىنڭىز خاتا بۇپ قالدى ، بۆلۈنگۈچى 0 بولسا بولمايدۇ ")
        pass