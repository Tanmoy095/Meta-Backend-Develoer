def find_factorial_by_looping (n):
    if n<0:
        return 0
    else:
        factorial=1
        for i in range(1,n+1):
            factorial=factorial*i
        return factorial
        
        
sol=find_factorial_by_looping(1)
print(sol)

def find_factorial_by_recursive(n):
    if n==1:
        return 1
        
    else:
        return n* find_factorial_by_recursive(n-1)
    
print(find_factorial_by_recursive(6))