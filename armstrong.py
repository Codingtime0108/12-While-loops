arm = int(input("Enter number less than 1000: "))
sum = 0
temp = arm
while temp > 0:
    ans = temp%10
    sum += ans ** 3
    temp //=10
    
if arm == sum:
        print(arm,"is an Armstrong number")
else:
            print(arm,"is an Armstrong number")
