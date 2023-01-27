global_list=[1,2,3,6]
# Traditional Function
# it's not a pure function as it changes the global_list by appending the item which is passed as an argument.
# In order to change it to a pure function, you need to think how to extend the function to accept
# a list as an argument, add the item to the list without modifying the original list,
# and how to return a new list with the newly added item.
def add_list(item):
    return global_list.append(item)

add_list(8)
print(global_list)


# A pure function is a function that does not change or have any effect on a variable, data, list, or sets 
# beyond its own scope. For example, if you have a list with the global scope, 
# a pure function cannot add something to that list or alter it in any way.
# pure Function
def add_to_list(list,item):
    l1=list.copy()
    l1.append(item)
    return l1

new=add_to_list(global_list,10)
print(new)
# This function is now a pure function because it adds value to a list, but it doesn't manipulate the original
# list outside the function. In this demonstration, you've learned what a pure function is and what you need 
# to do to change a function that's affecting a list on the global scope to a pure function that does not 
# interfere with the original list





# Firstly, with pure functions, you always know what the outcome will be. Pure functions are consistent
# snippets of code that do exactly what they are intended to do. Thirdly, pure functions include the 
# ability to cash since you know the return is always going to be the same. 
# Lastly, pure functions blend themselves well to a multi-threaded program. 
# In multi-threaded programs, more than one process can run concurrently, 
# which creates many threads of data. Pure functions will help prevent changes on the 
# global scope ensuring data stays reliable.