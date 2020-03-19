list=[]
n=int(input("Enter no. of elements you want to add - "))
print("Enter ",n," numbers - ")
for i in range(n):
    list.append(int(input()))
max=list[0]
for i in list:
    if(i>max):
        max=i
print("Largest No. is - ",max)