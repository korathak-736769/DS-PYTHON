import os
try:
    if os.path.exists(r"C:\Users\kolov\[ Python ]  Assignment\PYTHON_FILE\student.txt"):
        os.remove(r"C:\Users\kolov\[ Python ]  Assignment\PYTHON_FILE\student.txt")
        print("Delete Complete!!!")
    else:
        print("Don't found file !!")
except Exception as e:
    print(e)
        