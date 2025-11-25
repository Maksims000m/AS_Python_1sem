def a(b):
    return sum(b.values())

c = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print("Сумма значений:", a(c))  

def w(v):
    return {key: {} for key in v}

d = ['a', 'b', 'c']
print("Словарь из списка:", w(d)) 

def r(b):
    return len(set(b.values())) == 1

y = {'a': 1, 'b': 1, 'c': 1}
print("Все значения одинаковые:", r(y))  

ny = {'a': 1, 'b': 2, 'c': 1}
print("Все значения одинаковые:", r(ny))  
