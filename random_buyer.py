import random
name_string = input("Give me everybody's names, separated by comma")
name = name_string.split(", ")
random_choice= random.randint(0,(len(name)-1))
print(name[random_choice]+ " is going to buy the meal today.")
