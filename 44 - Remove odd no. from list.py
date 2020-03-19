def remodd(list):
    for i in list:
        if(i%2!=0):
            list.remove(i)
    return list

list=[]
n=int(input("Enter no. of items of list - "))
print("Enter list elements - ")
for i in range(n):
    list.append(int(input()))
list=remodd(list)
print(list)