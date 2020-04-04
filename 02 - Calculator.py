a=int(input("Enter first number - "))
b=int(input("Enter second number - "))
c=input("Enter operation - ")
if(c=='+'):
    print("Sum is ",a+b)
elif(c=='-'):
    print("Difference is ",a-b)
elif(c=='*'):
    print("Product is ",a*b)
elif(c=='/'):
    print("Qoutient is ",a/b)
    print("Remainder is ",a%b)
elif(c=='%'):
    print("Modulous is ",a%b)
elif(c=='^'):
    print(a," ^ ",b," = ",a^b)
else:
    print("Invalid Operator")
