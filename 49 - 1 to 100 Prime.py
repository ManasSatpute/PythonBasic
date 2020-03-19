def prime():
    for j in range(1,101):
        flag=0
        for i in range(2,j):
            if(j%i==0):
                flag=1
                break
        if(flag==0):
            print(j)

prime()