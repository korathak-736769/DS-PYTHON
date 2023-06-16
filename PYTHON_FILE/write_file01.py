file_write = open(r"C:\Users\kolov\[ Python ]  Assignment\PYTHON_FILE\score.txt","a",encoding='utf-8')
for i in range(5):
    name = str(input("Please input string : "))
    file_write.writelines(name+"\n")
file_write.close()