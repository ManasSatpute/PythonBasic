l=int(input("Enter any year - "))
if(l%4==0):
    if(l%100==0):
        if(l%400==0):
            print("Leap year.")
        else:
            print("Not a Leap year.")
    else:
        print("Not a Leap Year.")
else:
    print("Leap Year.")