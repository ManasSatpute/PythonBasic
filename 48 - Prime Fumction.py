def check(n):
    flag=0
    for i in range(2,n):
        if(n%i==0):
            flag=1
            break
    print("Composite Number.") if(flag==1) else print("Prime Number.")

n=int(input("Enter any No. - "))
check(n)