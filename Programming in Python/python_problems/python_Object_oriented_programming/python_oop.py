class Person:
    def __init__(self,person_name:str,date_of_birth:int,ht_inches:int=None) :
        
        self.__name = person_name;
        self.__year_of_birth = date_of_birth;
        self.__height = ht_inches
        
    def get_year_of_birth(self):
        return self.__year_of_birth
    
    def get_name(self):
        return self.name
    def set_name(self,new_name):
        if self.has_any_number(new_name):
            print("person name can't have number")
            return
        self.__name = new_name
    def has_any_number(self,string):
        return "0" in string
          
    def get_summary(self):
        return f"NAME:{self.__name}, DATE OF BIRTH:{self.__year_of_birth} , HEIGHT:{self.__height if self.__height is not None else 'Invalid'}"
    
person_list = [Person("Chintmmo",2008,6).get_summary(),
               Person("Tmr",1990).get_summary(),
               Person("Raan",1988,12).get_summary(),
               Person("Readmmy",1990,7).get_summary()
               ]

print(person_list)
# for person in person_list:
#      if person.get_year_of_birth() is not None and person.get_year_of_birth() >= 1990:
#          print(person.get_summary())