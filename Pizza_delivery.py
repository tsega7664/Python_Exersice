  ## Pizza Deliveries
print("welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, L\n")
add_pepperoni = input("Do you want pepperoni? Y, N\n")
extra_cheese = input("Do you want extra cheese? Y, N\n") 
if (size == "S" ):
    if (add_pepperoni == "Y"):
        if(extra_cheese == "Y"):
          
            print("Your final bill is $18.")
        else:
            print("Your final bill is $17.")
        print("your final bill is")
    else:
        print("Your final bill is $15.")    
elif(size == "M" ):
    if (add_pepperoni == "Y"):
        if(extra_cheese == "Y"):
          
            print("Your final bill is $24.")
        else:
            print("Your final bill is $23.")
    else:
        print("Your final bill is $20")
elif(size == "L" ):
    if (add_pepperoni == "Y"):
        if(extra_cheese == "Y"):
          
            print("Your final bill is $29.")
        else:
            print("Your final bill is $28.")
    else:
        print("Your final bill is $25.")
else:
    print("please check your choice")
      
