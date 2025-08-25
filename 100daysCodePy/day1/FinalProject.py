#build a code that build a Band name generator, ask the user for the city that they grew up in
#and the name of a pet. Combine the name of their city and pet and show them their band name.
city = input("What's name of the city you grew up in? \n")

print("Welcome to the Band Name Generator.")
print(city)

choose = input('do u have pet? yes or no. \n')

if choose == 'yes':
    pet = input('write your pet name: \n ')
    print(pet)
elif choose == 'no':
    pet = input('write your favorite animal: \n ')
    print(pet)

print('your band name it will be: \n ' + city + ' ' + pet)
