#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪


#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("welcome to the tip calculator!")
Bill_amt = input("What was the total bill? $")
Bill_amt = float(Bill_amt)
Tip_amt = input("How much tip would you like to give? 10, 12, or 15? ")
Tip_amt = float(Tip_amt)
Tip_per = Tip_amt/100
numerator = Bill_amt+(Tip_per*Bill_amt)
PeopleSplit_bill = input("How many people to split the bill? ")
PeopleSplit_bill = int(PeopleSplit_bill)
EachPer_bill_exc_tip = round(numerator/PeopleSplit_bill,2)

print(f"Each person should pay: ${EachPer_bill_exc_tip}")
