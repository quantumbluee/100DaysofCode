#If the bill was $150.00, split between 5 people, with 12% tip
print("Welcome to the tip calculator")
bill = input("What was the bill?\n")
tip = input("How much tip do you pay: 10%, 12% or 15%?\n")
num_people = input("How many people split the bill?\n")
 
tip_percent = int(tip)/100
total_tip = tip_percent * int(bill)
total_bill = int(bill) + total_tip
after_split = total_bill / 3
total = round(after_split,2)

print(f"The total amount to be paid by each person is {total}")
