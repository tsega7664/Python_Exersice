#tip calculator
print("Welcome to tip calculator.")
bill= float(input("What was the total bill?\n"))
per = int(input("What percentage tip would youlike to give?\n"))
people= int(input("How many people to split the bill?\n"))
value = ((per/100)*bill)+bill
final = value/people
final_amount= "{:.2f}".format(final)
print(f"Each person should pay ${final_amount} ")


  