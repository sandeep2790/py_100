print('''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
''')
print("Welcome to treasure island.")
print("Your mission is to find the treasure")
choice1 = input('You are at a crossroad, where you want to go? "left" or "right".').lower()

if choice1 == "left":
    choice2 = input('Stop! you need to cross lake choose "swim" or "wait" for boat.').lower()
    if choice2 == "wait":
        choice3 = input('choose door with color "yellow","red","blue".')
        if choice3 == "yellow":
            print("No luck, you are dead!")
        elif choice3 == "blue":
            print("Wrong door...!")
        else:
            print("you found treasure.")
    else:
        print("you are dead, shark waiting for dinner.")
else:
    print("Try next time!")
