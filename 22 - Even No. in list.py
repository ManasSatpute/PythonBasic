list=[]
n=int(input("Enter no. of terms you want to add in list - "))
for i in range(n):
    list.append(int(input()))
print("Even No. in the list are - ")
for i in list:
    if(i%2==0):
        print(i)