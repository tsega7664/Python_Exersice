#code to calculate how many days, weeks and monthes are left to bo 90.
currentAge = input(" what is your current age?")
year = 90 - int(currentAge)
week= int(year)*52
day = int(year)*365
month = int(year)*12
print(f"You have {day} days, {week} weeks and {month} months left")