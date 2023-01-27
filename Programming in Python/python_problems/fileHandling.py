import random
f = open("petnames.txt", "r")
f_content = f.read()
f_content_list = f_content.split("\n")
print(random.choice(f_content_list))

# Now that I have all my potential pet names in a list, I can randomly pick a name from the f_content_list of names.

# To do this, I'll need to import the random module at the top of my code: import random.

# Now I can use the random module's choice() function: random.choice().


f = open("petnames.txt", "r")
f_content = f.read()
print(type(f_content))
# f_content_list = f_content.split("\n")
# print(random.choice(f_content_list))




# Running the code now will output a random pet name. The first time I ran it, I got the name "Milo", 
# and the second time I ran it, I got the name "Dozer". It's always good to double-check your programs 
# like this by running them multiple times as a quick way to confirm that they behave as intended.




# Finally, If I had multiple files in my folder, I could allow myself to pick a file from which to read in a list of names.

# Here's how that would work

# import random
# f_name = input('Type the file name: ')
# f = open(f_name) # "r" omitted as it's the default
# f_content = f.read()
# f_content_list = f_content.split("\n")
# print(random.choice(f_content_list))