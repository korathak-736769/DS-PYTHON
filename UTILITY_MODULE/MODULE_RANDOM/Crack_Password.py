import random
ATM_PASSWORD = str(input("Please input password : "))
result = " "
count = 0
while result != ATM_PASSWORD:
    result = ""
    for letter in range(len(ATM_PASSWORD)):
        list_number = random.choice("0123456789")  
        # result="".join(list_number)+str(result) 
        result+=list_number
        # print("SEARCH : ",result)
    count+=1
    print("SEARCH[%d] : %s"%(count,result))
print("CRACK PASSWORD IS ",result)
