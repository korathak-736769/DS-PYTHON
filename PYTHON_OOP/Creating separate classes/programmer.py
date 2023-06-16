from employee import Employee
class Programmer(Employee):
    _department_name = 'System Development Department'
    def __init__(self,name,salary,experience,skill):
        super().__init__(name,salary,self._department_name)
        self.__exp = experience
        self.__skill = skill
        
    def _showData(self):
        super()._showData()
        print("Experience : {}".format(self.__exp))  
        print("Skill : {}".format(self.__skill))  
        
    def __str__(self):
        return super().__str__()+"\nExperience : {} \nSkill : {}\n".format(self.__exp,self.__skill)