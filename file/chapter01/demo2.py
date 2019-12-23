file_name="test2.txt"
file1=open(file_name,"w") # ئەگەر ھۆججەت كۆرستىلگەن ئادىرىستا يوق بولسا ، ئۆزى ھۆججەت قۇرىدۇ
res=file1.write("hello")# بىر قۇر مەزمۇن يېزىش
res=file1.write("\n")# قۇر ئالماشتۇرۇش
res=file1.write("world")# بىر قۇر مەزمۇن يېزىش
file1.close()