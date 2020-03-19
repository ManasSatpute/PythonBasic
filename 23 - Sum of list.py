list=[]
n=int(input("Enter no. of elements you want to add - "))
print("Enter ",n," numbers - ")
for i in range(n):
    list.append(int(input()))
sum=0
for i in list:
    sum+=i
print("Sum is - ",sum)