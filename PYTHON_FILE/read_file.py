file_read = open(r"C:\Users\kolov\[ Python ]  Assignment\PYTHON_FILE\student.txt","r",encoding='utf-8')
line = file_read.readlines()
for i in line:
    print('=>',i)

print(file_read.read())

