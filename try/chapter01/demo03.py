def read_file():
    try:
        file=open("test.txt","r")
        read=file.read()
        print(read)
    except:
        print("ھۆججەت ئۇقۇشتا خاتالىق بار")
    finally:
        """
          ئەگەر ئۈستىدىكى ھۆججەت ئۇقۇش نورمالسىزلىققا يۇلۇقسا ، except نىڭ ئىچىدىكى print ئۇچۇرى چىقسۇن.
          ئاندىن finally نىڭ ئىچدىكى جۈملە ئىجرا بولسۇن .
        """
        file.close()
        print("file close")
        pass

if __name__ == '__main__':
    read_file()