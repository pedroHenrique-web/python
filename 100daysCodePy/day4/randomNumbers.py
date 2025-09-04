import random

#random_integer = random.randint(1, 100)
#random_0_to_1 = random.random() * 10

#print(random_integer)
#print(random_0_to_1)

randomN = random.randint(1, 2)

choose = input('u want heads or tails?\n1 to heads and 2 to tails\n')

print(randomN)
if choose == 'heads' or choose == '1' and randomN == 1:
    print('//////////// heads, you win ////////////////')
elif choose == 'tails' or choose == '2' and randomN == 2:
    print('//////////// tails, u win ////////////////')
elif randomN == 2 and choose == 'heads' or choose == '1':
    print(f'/////// {randomN}, u lost /////////////')
elif randomN == 1 and choose == 'tails' or choose == '2':
    print(f'/////////////// {randomN}, u lost //////////////')
    

