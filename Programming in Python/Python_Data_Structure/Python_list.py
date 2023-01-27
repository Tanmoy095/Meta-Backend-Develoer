list1 = [1,2,3,4,5,6];
list2 = ["A","B","C"];
list3 = ["hello",True,40.2]
list4 = [1,[2,3,4],5]
#access to list
print(list1[2])

print(*list1)
print(list1,sep=",")
# The first option that I have is what's called the insert function. I can do list1.insert. 
# What it looks for is the index of where to insert to. Here I can use the LEN, or LEN function to get the length of the list1.
list1.insert(len(list1),7)
print(list1)
list1.append(10)
print(list1)
#adding multiple values to the list
list1.extend([12,13,14,14,15])
print(list1)
# deleting values from the list
# list1.pop(3);
del list1[4]
print(list1)


#  I can iterate through a list
# One of the main reasons I use lists is that I can iterate through the values and gain access to 
# large amounts of data. To iterate, I can use a simple four loop
for x in list1:
    print("value:",x)
    
# one important thing is list is mutable. i can change the value of list
    
list1[1]=22222;
print(list1)

