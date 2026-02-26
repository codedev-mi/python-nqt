def remove_duplicates(lst):
    converted = set(lst)
    return list(converted)
if __name__ == "__main__":
    lst = [1, 2, 3, 4, 4, 5, 5, 6]
    print(remove_duplicates(lst))
    