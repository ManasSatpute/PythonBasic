set=set()
n=int(input("Enter no. od elements of set - "))
print("Enter set 1 elements - ")
for i in range(n):
    set.add(input())
print("Before clearing - ",set)
set.clear()
print("After clearing - ",set)