def divided_by(a,b,):
    return a/b

try:
    ans = divided_by(40,0)
# except Exception as e :
# here zerroDivision error we get from print e.__class__
except ZeroDivisionError as e:
    print(e,"we cannot divide by zero")
except Exception as e :
    print(e,"something went wrong")
#Index Error 
# Starter code
items = [1,2,3,4,5]
item = items[6]
try:print(item)
except Exception as e :
    print(e,"something went wrong")
# print(e.__class__)
except IndexError as e :
    print(e,"list index out of range")
# file not found error
try:
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
except:
    print("Unable to locate file")
    

    
