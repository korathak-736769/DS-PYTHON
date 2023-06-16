PI =3.14
def summation(*args):
    total = 0
    for i in range(len(args)):
        total+=args[i]
    print("The result of plus is ",total)
    
def subtraction(num1,num2):
    print("The result of minus is ",num1-num2)

def power(num1,m):
    print(num1**m)