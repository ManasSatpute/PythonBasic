n=int(input("Enter last point - "))
for i in range(n+1):
    flag=int(0)
    for j in range(1,i):
        if(i%j==0):
            flag=int(flag+1)
    if(flag<=1):
        print(i)