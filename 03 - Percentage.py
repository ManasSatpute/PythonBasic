n=int(input("Enter no. of Subjects - "))
total=int(0)
print("Enter Marks Obtained and Max Marks for each Subject - ")
for i in range(n):
    m,mm=map(float,input().split())
    total+=m/mm
per=total/n*100
per="{:.2f}".format(per)
print("Percentage is -",per,"%")
