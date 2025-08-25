name = input('what is your name? ')
choose = None
newName = None

print(name)

choose = input(name + ' do u want to change your name? yes or no. ') 
 
if choose == 'yes':
    newName = input('write you new name: ') #new name of the user
    print('your new name is ' + newName)
elif choose == 'no':
    print('your name is still ' + name) #the same name of the usar before

choose = input('u want to know how many char exist in your name? yes or no. ')

if choose == 'yes':
    if newName != None: #if the user change a new name
        print('your new name have ' + str(len(newName)) + ' characters')
    elif name != None: #if the user not changed 
        print('your name have ' + str(len(name)) + ' characters')
elif choose == 'no':
    print('ok, bye, but your name have ' + str(len(name)) + ' characters')