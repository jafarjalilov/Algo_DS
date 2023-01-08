# https://www.codewars.com/kata/526571aae218b8ee490006f4
def count_bits(n):
    result = 0
    while n != 0:
        result += n % 2
        n //= 2
    return result

print(count_bits(1234))