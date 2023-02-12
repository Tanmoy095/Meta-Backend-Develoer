class Recipe():
    def __init__(self,dish,items,time) -> None:
        self.dish = dish
        self.items= items
        self.time= time
        
    def contents(self):
        print("The"+ self.dish +"has" + str(self.items)+  "and takes " + str(self.time))
        
pizza = Recipe("pizza","[cheese,meat,mutton]","50")
pasta = Recipe("pasta","[cheese,tomato,chicken]","50")


print(pizza.items)
print(pasta.items)

print(pizza.contents())

class MyFirstClass():
    print("Who wrote this?")
    index = "Author-Book"
    
    def hand_list(self,philosopher,book):
        print(MyFirstClass.index)
        print(str(philosopher)+ " wrote the book:" + str(book))
      
      
whodunnit = MyFirstClass()

whodunnit.hand_list("Sun Tzu","The Art of War")  
        
