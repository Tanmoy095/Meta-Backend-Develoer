class Employee():
    def __init__(self,name,last) -> None:
        self.name = name
        self.last = last
        
class Supervisor(Employee):
    def __init__(self, name, last,password) -> None:
        super().__init__(name, last)
        self.password = password
class Chefs(Employee):
    def leave_request(self,days):
        return "I want to leave for " +str(days) + "days"
    
    
    
adrian = Supervisor("adrian","A","Appleeeeee")

emily =Chefs("Emily", "e")
 
juno =Chefs("Juno", "J")

print(emily.leave_request(7))
print(adrian.password)
print(emily.name)