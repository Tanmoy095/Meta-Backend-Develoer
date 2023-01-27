favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']
for dessert in favorites:
    print("One of my favourite desert is ", dessert)
count =0;    
while count<len(favorites):
    print("One of my favourite desert is ", favorites[count])
    count+=1
    
# In many cases, you may need to search for a particular item in a list. Once the item is found, 
# there is no need to continue looping over the other results. Using the same example as before, 
# let's assume you only need to check if the dessert "Churros" is in the list and if it is, print a single statement. 
  
for dessert in favorites:
    if dessert == "Apple Pie":
     print("Yes!One of my favourite desert is ", dessert)
# But what happens if you look for a dessert and that dessert is not on the list?The code above is currently not set up to handle this.
# Let's look for the dessert "Pudding" which is not on the list, and also add an else statement to handle the case of when it's not found.
# If the dessert is not part of the list, you will print a new statement.
for dessert in favorites:
    if dessert == "Applee Pie":
     print("Yes!One of my favourite desert is ", dessert)
else:
    print('No sorry, that dessert is not on my list')

for i,x in enumerate(favorites):
    print(i,x)