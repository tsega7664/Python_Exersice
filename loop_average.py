height = input("Input a list of student heights\n ").split()
count = 0
sum = 0
for n in height:
    n = int(n)
    sum += n
    count= count+1
average = round(sum/count)
print(f"the average height of students is {average}")




## finding the highest score

score = input("Input a list of students score \n").split()

highest = 0
for s in score:
    s = int(s)
    if (s > highest):
       highest= s
print(f"The highest score in the class is: {highest}")



## finding the sum of even numbers from0-100
sum = 0

for n in range(2,101,2):
    sum +=n
print(sum)