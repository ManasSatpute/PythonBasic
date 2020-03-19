def checkeven(n):
    if(n%2==0):
        return True

a=int(input("Enter any Number - "))
print("Even No.") if(checkeven(a)) else print("Odd No.")