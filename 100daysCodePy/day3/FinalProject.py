print('wellcome to treasure island.')
print("you'are at a cross road. where do you want go?")
choose = input("     type 'left' or 'right'\n")

if choose == 'left':
    choose = input("you are at a lake, do you want to 'swim' or 'wait for a boat'?")
    if choose == 'swin':
        print('yu die')
elif choose == 'right':
    choose = input('ok, you arrived at a bridge and you see a duende, and he asks u a question: duende "what makes u come here, u want the treasure, right?" \n "type: yes or no"')
    if choose == 'yes':
        print('you die')
    elif choose == 'no':
        print('ok, you can go through')
        print('walking...')
        reponse = input('you see a blackboard, com this formula mathnmatics: "1+1",\n type the response:\n')
        if reponse =='11':
            print('you found the treasure!!!')
            choose = input('you want open? \n type: yes or no: \n')
            if choose == 'yes':
                print('you found a apple')
                choose = input('u want eat this apple?\n type: yes or no')
                if choose == 'yes':
                    print('u die ahhahaahhaahahhahaah, dumb')
                elif choose == 'no':
                    print('ok')
            elif choose == 'no':
                print('ok, see you later')
        else:
            print('you are dumb?, come back')
