year=input("Check Leap Year From Christmas:")
year=int(year)
if year%400==0 or year==1:

    print("Yes")
else:
    if year%4==0 and year%100!=0:
        print("Yes")
    else:
        print("No")
