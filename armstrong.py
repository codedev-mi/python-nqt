def armstrong(n):
    num = str(n)
    digits = len(num)
    sum = 0
    for i in num:
        sum += int(i) ** digits
    
    return sum == n

if __name__ == "__main__":
    n = 153
    if armstrong(n):
        print("true")
    else:
        print("false")