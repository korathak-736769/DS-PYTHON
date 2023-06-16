from employee import Employee
from acounting import Accounting
from programmer import Programmer
from sale import Sale

acount = Accounting("Sompong",43500,24)
programmer = Programmer("Jhon",18900,'5 year','Python , Php , Java')
sale = Sale("Diva",67900,'Thailand')

# print(acount.__str__())
# print(programmer.__str__())
# print(sale.__str__())

print("Department_Acount     [Annual_Income] : {}".format(acount._get_Income(999)))
print("Department_Programmer [Annual_Income] : {}".format(programmer._get_Income(2342,500)))
print("Department_Sale       [Annual_Income] : {}".format(sale._get_Income()))