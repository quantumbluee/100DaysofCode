from art import logo, vs
from game_data import data
import random
from replit import clear

def display_names(person):
  '''Displays name in the required format'''
  account_name = person["name"]
  description = person["description"]
  country = person["country"]
  return f"{account_name}, a {description} from {country}"
  
def check_answer(choice, a_followers,b_followers):
  '''Use if statement to see if choice is correct'''
  if a_followers > b_followers:
    return choice == 'a'
  else:
    return choice == 'b'
  
#display Art
print(logo)
score = 0
continue_game = True
B = random.choice(data)

while continue_game:
  A = B
  B = random.choice(data)
  if A == B:
    B = random.choice(data)
  
  print(f"Compare A: {display_names(A)}")
  print(vs)
  print(f"Against B: {display_names(B)}")
  
  #ask for guess
  choice = input("Who has more followers? \n A or B?").lower()
  
  #check and give score
  a_followers = A["follower_count"]
  b_followers = B["follower_count"]
  
  is_correct = check_answer(choice,a_followers,b_followers)
  clear()
  
  if is_correct:
    score += 1
    print(f"You're right. Current score: {score}")
    
  else:
    continue_game = False
    print(f"You're wrong. Final score: {score}")
