import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
game_img = [rock, paper, scissors]
user_input = int(input("choose one option : 0 for Rock, 1 for Paper, 2 for scissor \n"))
if user_input >= 3 or user_input < 0:
  print("Please select right choice!")
else:
  print(game_img[user_input])
  
  computer_input = random.randint(0, 2)
  print("computer chose:")
  print(game_img[computer_input])
  
  
  if user_input == 0 and computer_input == 2:
    print("You Win")
  elif computer_input == 0 and user_input == 2:
    print("You Lose")
  elif computer_input > user_input:
    print("You Lose")
  elif user_input > computer_input:
    print("You Win")
  elif computer_input == user_input:
    print("It's a Draw")
  