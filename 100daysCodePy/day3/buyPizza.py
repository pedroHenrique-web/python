# make the program that make 3 questions for the user and calculate how much the pizza will cost, is the user want Large pizza, small or medium, add pepperoni or extra cheese.

print('welcome to Python Pizza Deliveries!')

size = input('you want a small, medium or large pizza? S, M or L. ')
bill = 0

if size != 'S' and size != 'M' and size != 'L':
    print('Shut up bro, no kiding me')
    print('your bill is: one million dollars')
    
else:
    add_pepperoni = input('u want pepperoni? yes or no. ')
    extra_cheese = input('u want extra cheese? yes or no. ')

    if size == 'S':
        bill = 15
    elif size == 'M':
        bill = 20

    elif size == 'L':
        bill = 25
    if add_pepperoni == 'yes':
        if size == 'S':
            bill += 2
        else:
            bill += 3
    if extra_cheese == 'yes':
        bill += 1
    print(f'your final bill is: ${bill}')

