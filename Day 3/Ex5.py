# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1.lower()
name2.lower()
true1 = name1.count('t') + name1.count('r') + name1.count('u') + name1.count('e')
true2 = name2.count('t') + name2.count('r') + name2.count('u') + name2.count('e') 
true = true1+true2
love1 = name1.count('l') + name1.count('o') + name1.count('v') + name1.count('e')
love2 = name2.count('l') + name2.count('o') + name2.count('v') + name2.count('e')
love = love1+love2

true_love = 10*true + love
if true_love<10 or true_love>90:
    print(f"Your score is {true_love}, you go together like coke and mentos")
elif 40<true_love<50:
    print(f"Your score is {true_love}, you are alright together")
else:
    print(f"Your score is {true_love}")
