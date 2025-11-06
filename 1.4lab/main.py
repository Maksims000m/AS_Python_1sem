# На месте c любой список
def a(s):
    b = any(num % 2 != 0 for num in s)
    if b:
        return [0 if num % 2 != 0 else num for num in s]
    return s
c = [1, 2, 3, 4, 5]
d = a(c)
print(d)
