def binary_addition(bin_a, bin_b):
    a = int(bin_a, 2)
    b = int(bin_b, 2)

    if bin_b[0] == '1':  
        b = -((1 << len(bin_b)) - b)  

    result = a + b

    if result >= 0:
        return bin(result)[2:]
    else:
        return bin((1 << (len(bin_a) + 1)) + result)[2:]

 # Пример: положительное число 27 (11011) и отрицательное число -17 (11101111)
def main():
    positive_bin = '11011'
    negative_bin = '11101111'

    sum_result = binary_addition(positive_bin, negative_bin)
    
    print(f"Сумма {positive_bin} и {negative_bin} в двоичной системе: {sum_result}")

if __name__ == "__main__":
    main()
