#declaration of the list
my_list =[10,20,3,2,8,6]
#we initialize the total value which will store the sum to zero
Total=0
#the for loop to count progressively the elements of the list starting from 0
for i in range(0,len(my_list)):
    Total+=my_list[i]
#using the index i which is replaced the elements ,they will add all of them and assign to the variable total
print(f"The sum of elements in this list : {my_list} is: {Total}")