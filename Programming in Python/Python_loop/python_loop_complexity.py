# I print out zero, and then I use end equals and a string with space in double quotes to ensure 
# it prints out in an even manner. Lastly, I'm going to print out an empty line so that it goes to a new line
# in each iteration. If I run the for loop, the system prints out a 2D array grid. 
# This is just the demonstrates how the for loop works. 

import time 
start_time =time.time();
# outer loop
for i in range(2):
    # inner loop
    for j in range(10):
        print(0,end = " ")
    print()
    
print(round((time.time()-start_time),2))


input(j)