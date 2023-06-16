#  Module Date & Time
import datetime
result = datetime.datetime.now()
# print(result) # show all time 
# print(result.year) # show year time 
# print(result.month) # show month time 
create_date = datetime.datetime(2023,12,6,12,34) #create time 
# print(create_date)
# -------------------------------------------------------------
# display format
print("Start : ",result)
print(result.strftime("%x")) # m/d/y type short
print(result.strftime("%X")) # time type short
print(result.strftime("%c")) # time type long

print(result.strftime("%H")) # time 
print(result.strftime("%H:%M:%S %p")) # time 

# 1 - 366
print(result.strftime("%j")) # time

# date (variable : create_date)
print(create_date.strftime("%a")) #short
print(create_date.strftime("%A")) #long
print(create_date.strftime("%w")) # 0 = sunday
print(create_date.strftime("%d")) # date
print(create_date.strftime("%b")) # short month
print(create_date.strftime("%B")) # long month

print(create_date.strftime("DATE : %d , %A MONTH : %B , YEAR : %Y")) # long month

# DATE/MONTH/YEAR
print(create_date.strftime("%d/%m/%y")) # long month

