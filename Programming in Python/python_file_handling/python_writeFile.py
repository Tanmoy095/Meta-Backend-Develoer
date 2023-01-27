#  In Python, we can create new files using the open function and enabling the write mode.
# I can begin to add content to the file using the write function. On a new line, I type file.write. 
# I'm going to add some simple text. This is a new file created. 
# with open("newFile.txt", "w") as file:
#     file.write("My new file created by python!")
# If I choose to write multiple lines of contents of the file instead of a single line, 
# I can use the Writelines function. The Writelines function accepts a list. A list in Python is 
# represented by square brackets and then a comma for each line. I edit my file.write to say 
# file.writelines. Then within square brackets,
# \n for new line
with open("newFile.txt", "w") as file:
     file.writelines(["My new file created by python!","\nThis is another line to be added"])
    
# if I want to add to the file as opposed to replacing it each time, I just need to change the action
# of mode. To do so, I replace the letter w and put in a letter a, which stands for append. 
# and I click Run three times. I check the file and confirm that the new lines were appended each time
try:
    with open("newFile.txt", "a") as file:
        file.writelines(["\nMy new file created by python!","\nThis is another line to be added"])
except FileNotFoundError as e:
    print("error",e)