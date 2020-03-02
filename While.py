a=int(input("Enter a number - "))
sum=int(0)
while(a!=0):
    sum+=int(a%10)
    a=int(a/10)
print("Sum of digits is - ",sum)