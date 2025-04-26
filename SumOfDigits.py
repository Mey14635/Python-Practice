num=int(input("Enter the number : "))
#we initialize the variable that will receive the total to 0
Sum_var=0
while num>0:
    #the modulo operation give as the reminder of division means it will give only the last no
#if the number is 234 the reminder will be 4
    reminder=num%10
    Sum_var=Sum_var+reminder
    #then we add the sum of variable (initially 0),then we use the division to get an integer number of the digits enter(the first ones)
    num=num//10
    #all that will happen as long as the num is greater than 0
print("The sum of digit is : ",Sum_var)