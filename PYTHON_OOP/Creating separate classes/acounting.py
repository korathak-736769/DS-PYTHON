from employee import Employee
class Accounting(Employee):
    _department_name = 'accounting department'
    def __init__(self,name,salary,age):
        super().__init__(name,salary,self._department_name)
        self._age = age
        
    def _showData(self):
        super()._showData()
        print("Age : {}".format(self._age))        
    
    # Another form can be written as follows: 
    def __str__(self):
        return super().__str__()+"\nage : {}\n".format(self._age)