# а
def filter_numbers(numbers, condition=None):
    if condition is None:
        return numbers
    return [num for num in numbers if condition(num)]


print(filter_numbers([1, 2, 3, 4, 5])) 
print(filter_numbers([1, 2, 3, 4, 5], condition=lambda x: x % 2 == 0)) 






# б
def transform_numbers(numbers, transform_function=None):
    if transform_function is None:
        return numbers
    return [transform_function(num) for num in numbers]


print(transform_numbers([1, 2, 3])) 
print(transform_numbers([1, 2, 3], transform_function=lambda x: x ** 3)) 






# в
def cube_numbers(*args):
    return [num ** 3 for lst in args for num in lst]


print(cube_numbers([1, 2], [3, 4])) 
print(cube_numbers([5], [6, 7], [8])) 






# г
def product_non_zero(*args):
    product = 1
    has_non_zero = False

    for num in args:
        if num != 0:
            product *= num
            has_non_zero = True

    return product if has_non_zero else 1


print(product_non_zero(1, 2, 0, 4)) 
print(product_non_zero(0, 0, 0)) 
