a,b,c=map(int,input("Enter 3 No. - ").split())
if(a>=b and b>=c):
    print(a," is greatest.")
elif(b>=c and b>=a):
    print(b," is greatest.")
else:
    print(c," is greatest.")