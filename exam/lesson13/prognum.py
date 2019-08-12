def func(n):
    if n <= 0:
        return None
        
    elif n==1 or n==2:
        return 1
    else:
        return func(n-2)+func(n-1)
        
    
        

        
        