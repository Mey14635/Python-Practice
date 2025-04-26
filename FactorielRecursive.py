number=int(input("Enter the the number : "))
#the factories of 0 and 1 is 1 so the first case is compare and initialize the number  enter to 1 or 0
factorial=1
if number==0 or number ==1:
    print(f"The factorial of {number} is 1")
else:
#  the for loop will start from 1 till the number enter plus an extra number to include the no entered
    for i in range(1,number+1):
       factorial=factorial*i
#if the no entered is 2 initially the fact is 1 ie 1*1,back to the loop then 1*2 will be store in the fact and so on
print(f"The factorial of {number} is : {factorial} ")