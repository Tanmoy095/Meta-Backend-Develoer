my_sets = {1,2,3,4,5,6,6,7};
my_sets2 = {4,5,6,10,11,12}

#  Sets differ slightly from lists, in that they don't allow duplicate values. 
# I can demo this by putting in another 5, when I click on run, I find that the second 6 is not 
# printed out in the list. 
print(my_sets);
# Sets also have methods that we can use, I can use a method to add new content. If I use set_a.add (6),
my_sets.add(10);
print(my_sets);


# I could also use the remove method, I'll remove the number 2, when I clicked on run, 
# I found the number 2 was removed from the set.
my_sets.remove(2);
print(my_sets);
# There's also discard, which essentially does the same thing as remove. Using discard, 
# when I click on run I'll find that I get the same output.
my_sets.discard(2);
print(my_sets);

new_sets = my_sets.intersection(my_sets2)
print(new_sets)