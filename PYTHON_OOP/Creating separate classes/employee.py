class Employee:
    #class variable
    _max_salary = 50000
    __min_salary = 15000
    _company_name = 'umbrella'
    def __init__(self,emp_name,emp_salary,emp_department):
        self.__name = emp_name
        self.__salary = emp_salary
        self._department = emp_department
        
    # annual income
    def _get_Income(self):
        return self.__salary*12
    
    def _get_Income(self,bonus=0,overtime=0):
        return (self.__salary*12)+bonus+overtime
    
    def __str__(self):
        return ("Employee_name : {} \nSalary : {} \nDepartment : {} \nAnnual_Income : {}".format(self.__name,self.__salary,self._department,self._get_Income()))
    
    #protected method
    def _showData(self):
        print("Employee_Name : {}".format(self.__name))
        print("Salary : {}".format(self.__salary))
        print("Department : {}".format(self._department))