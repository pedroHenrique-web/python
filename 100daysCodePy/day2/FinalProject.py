#imagine you are at a restaurant, the waiter brings the check and you decide how much you want to tip (10%, 12% or 15%), how many peoples have in your group and make the program that how much each person should pay.

bill = float(input('how much was the bill? '))
tip = float(input('how much do you want to pay for the tip? 10, 12 or 15? '))
peoples = int(input('how many peoples have in your group? '))


if tip == '10':
    tip = bill * 0.1
elif tip == '12':
    tip = bill * 0.12
elif tip == '15':
    tip = bill * 0.15

print(f"you tip is ${tip}")

bill = bill + tip
bill_for_person = (bill / peoples)

print(f'the bill for person is ${bill_for_person:.2f}')

