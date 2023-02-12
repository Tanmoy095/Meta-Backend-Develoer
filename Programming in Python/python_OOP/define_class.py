class House:
    num_rooms = 5;
    num_bathroom = 2;
    def cost_evaluation(self,rate):
        cost = rate*self.num_rooms
        return cost
        
        
        
house = House()
print(house.num_rooms)
print(House.num_rooms)
house.num_rooms = 7
# House.num_rooms = 7
print(house.num_rooms)
print(House.num_rooms)

print(house.cost_evaluation(12))

value = 7
class A:
    value = 5
a = A()
a.value = 3
print(a.value)

# bravo = 3
# b = B()
# class B:
#     bravo = 5
#     print("Inside class B")
# c = B()
# print(b.bravo)