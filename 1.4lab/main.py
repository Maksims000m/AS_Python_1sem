def a(lst):
    b = any(num % 2 != 0 for num in lst)
    if b:
        return [0 if num % 2 != 0 else num for num in lst]
    return lst
c = [1, 2, 3, 4, 5]
d = a(c)
print(d)
