number1 = None
number2 = None
choice = None

print("hello " + input("What is your name? ")+ '!') 
print("Welcome to the tip calculator.")

number1 = float(input("write a number "))
number2 = float(input("write another number "))

choice = input("u want to add, subtract, multiply or divide? ")

if choice == 'add':
    print('the additon is: ' + str(number1 + number2))
elif choice == 'subtract':
    print('the subtract is: ' + str(number1 - number2))
elif choice == 'multiply':
    print('the multiply is: ' + str(number1 * number2))
elif choice == 'divide':
    print('the division is: ' + str(number1 / number2))
else:
    print('u not choose a valid option')





