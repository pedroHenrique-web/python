#paper =print("( \_/)\n( •_•)\n/ >[]") 2
#scissors = print("(\_/)\n( •_•)\n/ >8<") 1
#rock = print("( \_/)\n( •_•)\n/ >O<") 0
import random


randomJG = random.randint(0, 2)
choose = input("wellcome to jokenpo game, u need to choose 3 options \n///// 0 for rock \n///// 1 for scissors\n///// 2 for paper\n which u choose? ")

    #rock
if choose == '0' and randomJG == 2:
    print("you, rock:\n( \_/)\n( •_•)\n/ >O<")
    print("me, paper:\n( \_/)\n( •_•)\n/ >[]")
    print('u lost')
elif choose == '0' and randomJG == 1:
    print("you, rock:\n( \_/)\n( •_•)\n/ >O<")
    print("me, scissors:\n(\_/)\n( •_•)\n/ >8<")
    print('u wins') 
elif choose == "0" and randomJG == 0:
    print("you, rock:\n( \_/)\n( •_•)\n/ >O<")
    print("me, rock:\n( \_/)\n( •_•)\n/ >O<")
    print('we tied')
    #scissors
elif choose == '1' and ran2domJG == 2:
    print("you, scissors:\n(\_/)\n( •_•)\n/ >8<")
    print("me, paper:\n( \_/)\n( •_•)\n/ >[]")
    print('u wins')
elif choose == '1' and randomJG == 0:
    print("you, scissors:\n(\_/)\n( •_•)\n/ >8<]")
    print("me, rock:\n( \_/)\n( •_•)\n/ >O<")
    print('u lost')
elif choose == '1' and randomJG == 1:
    print("you, scissors:\n(\_/)\n( •_•)\n/ >8<")
    print("me, scissors:\n(\_/)\n( •_•)\n/ >8<")
    print('we tied')
    #paper
elif choose == "2" and randomJG == 0:
    print("you, paper:\n( \_/)\n( •_•)\n/ >[]")
    print("me, rock:\n( \_/)\n( •_•)\n/ >O<")
    print('u wins')
elif choose == "2" and randomJG == 1:
    print("you, paper:\n( \_/)\n( •_•)\n/ >[]")
    print("me, scissors:\n(\_/)\n( •_•)\n/ >8<")
    print('u lost')
elif choose == "2" and randomJG == 2:
    print("you, scissors:\n(\_/)\n( •_•)\n/ >8<")
    print("me, scissors:\n(\_/)\n( •_•)\n/ >8<")
    print('we tied')