Fibarray = [0,1]
def fibonacci(n):
    if n < 0:
        print("Incoreect Output")
    
    elif n < len(Fibarray):
        return Fibarray[n]
    
    else:
        Fibarray.append(fibonacci(n-1)+fibonacci(n-2))
    return Fibarray[n]

print(fibonacci(9))


