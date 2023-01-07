# https://www.codewars.com/kata/526571aae218b8ee490006f4
def count_bits(n):
    result = 0
    while n != 0:
        bit = n % 2
        if bit == 1:
            result += 1
        n //= 2
    return result

print(count_bits(1234))