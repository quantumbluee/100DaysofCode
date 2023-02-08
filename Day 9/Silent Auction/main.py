from replit import clear
import operator
import art
print(art.logo)
silent_auction = {}
auction = True
while auction is True:
  name = input("What is your name? ")
  bid = input("What is your bid? ")
  silent_auction[name] = bid
  bidders = input("Are there any other bidders left to bit? Y/N").lower()
  clear()
  if bidders == "y":
    auction = True 
  else:
    auction = False
    keyMax = max(silent_auction.items(), key =   operator.itemgetter(1))[0]
    print(f"Winner of the auction is {keyMax}")
