def vowel(str):
    v = 0
    c = 0
    vowels = "aeiouAEIOU"

    for char in str:
        if char.isalpha():
            if char in vowels:
                v += 1
           
            else:
                c += 1
    return v ,c
    
if __name__ == "__main__":
    str = "Hello World"
    print(vowel(str))
    
