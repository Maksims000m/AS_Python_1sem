def modulus(complex_num):
    """Вычисляет модуль комплексного числа."""
    return abs(complex_num)
def multiply(complex_num1, complex_num2):
    """Умножает два комплексных числа."""
    return complex_num1 * complex_num2
def divide(complex_num1, complex_num2):
    """Делит одно комплексное число на другое."""
    if complex_num2 == 0:
        raise ValueError("Деление на ноль не допускается.")
    return complex_num1 / complex_num2

# Пример модуля, умножения и деления

from complex_operations import modulus, multiply, divide
z1 = complex(3, 4) 
z2 = complex(1, 2) 
    
m_z1 = modulus(z1)
print(f"Модуль {z1} = {d_z1}")
    
p = multiply(z1, z2)
print(f"{z1} * {z2} = {p}")
    

try:
    q = divide(z1, z2)
    print(f"{z1} / {z2} = {q}")
except ValueError as e:
    print(e)


