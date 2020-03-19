def sum(list):
    sum=0
    for i in list:
        sum+=i
    return sum

list=[]
n=int(input("Enter no. of elements in list - "))
print("Enter numbers - ")
for i in range(n):
    list.append(int(input()))
print("Sum of list is - ",sum(list))