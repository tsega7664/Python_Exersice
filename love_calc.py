print("Welcome to the Love Calculator")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
count = 0
count1 = 0
combined_String = name1 + name2
name1_lower = combined_String.lower()
count += name1_lower.count("t")
count += name1_lower.count("r")
count += name1_lower.count("u")
count += name1_lower.count("e")
count= str(count)
name2_lower = combined_String.lower()
count1 += name2_lower.count("l")
count1 += name2_lower.count("o")
count1 += name2_lower.count("v")
count1 += name2_lower.count("e")
count1 = str (count1)
total = count + count1
total = int(total)
if total < 10 or total > 90:
    print(f"Your Score is {total}, you go together like coke and mentose")
elif total >= 40 and total <=50:
    print(f"your Score is {total}, you are alright together")
else:
    print(f"your Score is {total}")

