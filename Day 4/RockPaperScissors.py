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
game_images=[rock,paper,scissors]
user_input = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors: \n"))
if user_input in range(0,2):
  print(game_images[user_input])
  computer_choice = random.randint(0,2)
  print("The computer chose: ")
  print(game_images[computer_choice])
else:
  print("Choose a valid number")


if user_input>3 or user_input<0:
  print("You typed an invalid number, you lose.")
elif user_input==0 and computer_choice==2:
  print("User wins!")
elif computer_choice==0 and user_input==2:
  print("You lose")
elif computer_choice>user_input:
  print("The computer wins!")
elif user_input>computer_choice:
  print("You win!")
elif computer_choice==user_input:
  print("It's a draw!")
