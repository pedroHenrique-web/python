heigth = float(input('what is your height in cm? '))
bill = 12


if heigth >= 120:
    print('you can ride the rollercoaster') 

    age = int(input('what is your age? '))
    if age < 12:
        bill = 5

        print('please pay $5')
    elif age <= 18:
        bill = 7

        print('please pay $7')
    else:
        bill = 12

        print('please pay $12')

    want_photo = input('do you want a photo taken, is $3 dollars? yes or no. ')
    if want_photo == 'yes':
        bill += 3
    
    print(f'your final bill is ${bill}')
else: 
    print('sorry you have to grow taller before you can ride')