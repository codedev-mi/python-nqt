def factorial(n):
    ans = 1
    i = 2
    while (i <= n):
        ans *= i
        i += 1
    return ans
if __name__ == "__main__":
    n = 5
    print(factorial(n))