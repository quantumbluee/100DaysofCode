print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print("Your goal is to find the treasure.")
choice1 = input("You are confronted with two paths: in which direction do you go, 'left' or 'right'?\n").lower()
# swim = input("You see a lake in front of you? Do you swim or wait?")
# swim.lower()
# door = input("You see 3 doors in front of you: red, blue and yellow. Which door do you choose?")
# door.lower()


if choice1 == 'left':
  choice2 = input("You see a lake in front of you? Do you swim or wait?\n").lower()
  if choice2 == 'wait':
    choice3 = input("You see 3 doors in front of you: red, blue and yellow. Which door do you choose?\n").lower()
    if choice3 == 'red':
      print("Burnt like a steak. GAME OVER")
    elif choice3 == 'yellow':
      print("You found the treasure! You win")
    elif choice3 == 'blue':
      print("You were eaten by beasts. GAME OVER")
    else:
      print("There are just 3 doors. GAME OVER.")
  else:
    print("Oh! You were attacked by a trout. GAME OVER")
else:
  print("Oh! The path you chose just led to death. GAME OVER")
