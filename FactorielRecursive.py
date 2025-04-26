n=int(input("Enter the the number : "))
def fact(n):
#we check and compare the no entered if is the initial value cause fact of 0 and 1 is 1
    if n==1:
        return 1
    else:
#otherwise we will recall the function but with the smaller following number until get the base case (1)
        return n*fact(n-1)
print("The factories is: ",fact(n))