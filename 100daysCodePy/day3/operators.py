print(2 + 3)
print(4 -7)
print(9.4 / 5)

#value without decimal
print(9.4 // 5)

#exponentiation
print(2 ** 8)

#modulo
print(10 % 3)

#odd or even

odd_even = float(input('write a integer number, and will know if it is odd or even: '))

odd_even = odd_even % 2

if odd_even == 0:
    print('this number is even')
elif odd_even != 0 and odd_even != 1:
    print('this is not a integer number')
else:
    print('this number is odd')
