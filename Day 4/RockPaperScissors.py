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
user_input = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors: \n"))
computer_choice = random.randint(0,2)
print(f"The computer chose {computer_choice}")

if user_input==0 and computer_choice==2:
  print("User wins!")
elif computer_choice>user_input:
  print("The computer wins!")
else:
  print("We are playing rock paper scissors dude")
