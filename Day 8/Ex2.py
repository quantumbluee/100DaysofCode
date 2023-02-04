#Write your code below this line 👇

def prime_checker(number):
    factors = 0
    if number == 1:
        print("It's not a prime number")
    for nums in range(1,number):
        if number % nums == 0:
            factors+=1 
    if factors>2:
        print("It's not a prime number")
    else:
        print("It's a prime number")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
