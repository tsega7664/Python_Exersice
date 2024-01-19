def prime_checker(num):
    count = 0
    for i in range(2,num):
        if (num%i==0):
            count= count+1
    if(count > 0):
        print(f"\n {num} is not a prime number.")
    else:
        print(f"\n {num} is a prime number.")
n = int(input("enter thr number:\t"))
prime_checker(num=n)