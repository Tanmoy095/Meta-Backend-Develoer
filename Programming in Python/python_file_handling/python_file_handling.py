# There are two file handling functions in Python, open and close. Let's explore the open function first. 
# The open function is used for reading, writing and creating files.

# The open function accepts two arguments. 
# The first is the file name and or the file location and the second argument is the mode.
# open finction 
# open(<FILE_NAME><FILE_LOCATION>,<MODE>)


# The mode indicates what action is required such as reading, writing or creating. 
# It's also specifies if you want the file output in text or binary format. 
# Let's explore the modes of file handling you can use in Python. 

# MODE SETS
# mode = "r" or mode = "r+"
# First you have r which is used to open and read a file in text format and to rb opens and 
# reads a file in binary format. You will learn more about this later. 
# R+ on the other hand,opens the file for both reading and writing 
# and w opens the file for writing. Note that w will overwrite the existing file.
# Lastly, a opens files for editing or appending data.

# Next, there's the close function. The close function is used for closing the open file connection, 
# know that it does not take any arguments.    close()

# There is one more way to open and close a file in Python and that's with open function. T
# he advantage of using it is that it closes the file automatically. 
# ex::::--with open ("testing.txt","r") as file

# In Python, you generally handle files in two ways, either in text or binary format
# The text format is more user friendly because humans can read. You won't be able to read files in binary formats, but they are much more compact and therefore result in better performance. 

# 1st way ex:::
file = open('test.txt',mode = 'r')
data = file.readline()
print(data)
file.close()

with open ("testing.txt","r") as file:
    data = file.readline()
    print(data)