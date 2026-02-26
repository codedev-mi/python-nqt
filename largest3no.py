# def largest_of_three(a, b, c):
#     if a >= b and a >= c:
#         return a
#     elif b >= a and b >= c:
#         return b
#     else:
#         return c

# print(largest_of_three(10, 25, 15))


def largestnum(n):
    return int(''.join(sorted(str(n), reverse=True)))

print(largestnum(1234))