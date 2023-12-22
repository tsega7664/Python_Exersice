#code to calculate BMI
height = input("enter your height in m:")
weight = input("enter your weight in kg:")
result = float(weight)/(float(height)*float (height))
final= round(result,2)
if (final<18.5):
    print(f"Your BMI is {final} and you are Underweight.")
elif (final<25):
    print(f"Your BMI is {final} and you have Normal weight.")
elif (final <30):
    print(f"Your BMI is {final} and you are Overweight.")
elif ( final<35):
        print(f"Your BMI is {final} and you are Obese.")
else :
         print(f"Your BMI is {final} and you are Clinically obese .")