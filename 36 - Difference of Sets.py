set1=set()
set2=set()
n=int(input("Enter no. od elements of set 1 - "))
print("Enter set 1 elements - ")
for i in range(n):
    set1.add(input())
m=int(input("Enter no. od elements of set 2 - "))
print("Enter set 1 elements - ")
for i in range(m):
    set2.add(input())
print("Set 1 - ",set1)
print("Set 2 - ",set2)
print("Set1 - Set2 = ",set1.difference(set2))
print("Set2 - Set1 = ",set2.difference(set1))