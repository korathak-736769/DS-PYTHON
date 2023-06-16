from employee import Employee
class Sale(Employee):
    _department_name = 'Sales Department'
    def __init__(self,name,salary,area):
        super().__init__(name,salary,self._department_name)
        self._area = area

    def _showData(self):
        super()._showData()
        print("Area : {}".format(self._area))
        
    def __str__(self):
        return super().__str__()+"\nArea : {}\n".format((self._area))

class define():
    pass