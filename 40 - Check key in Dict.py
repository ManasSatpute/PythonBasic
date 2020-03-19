dict = {'Name':'Mark','Age':'26','Roll No.':'CS150','Address':'India'}
print(dict)
ch=input("Enter Key to be Searched - ")
keys=dict.keys()
flag=0
for i in keys:
    if(ch==i):
        flag=1
print("Key Does Not Exist.") if(flag==0) else print("Key Exists.")
