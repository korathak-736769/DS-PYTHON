file_write = open(r"C:\Users\kolov\[ Python ]  Assignment\PYTHON_FILE\score.txt","r",encoding='utf-8')
line = file_write.readlines()
for i in line:
    print('=>',i)
file_write.close()

file_write = open(r"C:\Users\kolov\[ Python ]  Assignment\PYTHON_FILE\score.txt","w",encoding='utf-8')
# ถ้าเป็น w เป็นการนำข้อมูลไปแทนที่
file_write.writelines('Computer Engineer\n')
file_write.close()
file_write = open(r"C:\Users\kolov\[ Python ]  Assignment\PYTHON_FILE\score.txt","a",encoding='utf-8')
# ถ้าเป็น a เป็นการนำข้อมูลไปต่อท้าย
file_write.writelines('Hello Programming')
file_write.close()
# when you click runing program will create a new file 