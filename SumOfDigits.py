num=int(input("Enter the number : "))
Sum_var=0
while num>0:
    rem=num%10
    Sum_var=Sum_var+rem
    num=num//10
print("The sum of digit is : ",Sum_var)