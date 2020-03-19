def printFibo(n):
    n1=0
    n2=1
    for i in range(n):
        print(n1)
        temp=n1
        n1=n2
        n2=temp+n2

n=int(input("Enter No. of terms you want to print - "))
printFibo(n)