
# A tuple can accept any mix of data types.
my_tuple = (1,True,"hello","hello",1.2)
print(my_tuple[1])
# Tuples also provide different methods of count and index. I can do my underscore tuple dot count and passing
# the value of strings. I click on run and I get back to count of one. What it does is it looks for the number
# of occurrences of that value within the tuple
print(my_tuple)

print(my_tuple.count("hello"))

# The other method is index, which would give me back the index of where the value lies in the tuple. 

print(my_tuple.index(1.2))
# I can also do a loop manageable. That is iterate through the values and print them out. 
# I can write a loop for X in my underscore tuple and then print out the value of X
for x in my_tuple:
    print(x)
    
# The one key difference of a tuple over a list is that tuple values are what's called immutable.
# And this just means that they cannot be changed. 
my_tuple[1] = 1111
print(my_tuple)
# If I run this, I'll get back an error. And it gives me the error saying type error, 
# tuple object does not support item assignment. That's because anything that is declared in a tuple is immutable