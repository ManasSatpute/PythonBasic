set={'1','2','3','4','5'}
print(set)
n=int(input("No. of values to be removed - "))
for i in range(n):
    x=input("Value to be removed - ")
    set.discard(x)
print(set)