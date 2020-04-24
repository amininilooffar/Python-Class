day = int (input ('enter the day number:'))
month = int (input ("enter the month number:"))
year = int (input('enter the year:'))

if month < 3 :
    if month == 1:
        Summary= day
        print("Summary is:")
        print (Summary)
    else:
            Summary= day + 31
            print(Summary)
            
else:
    if year%400==0:
        Summary= day + (month//2)+ ((month-2)*30)+29
        print("Summary is:")
        print(Summary)
        print("leap year")
    elif year%4== 0 and year%100!=0:
        Summary= day + (month//2)+ ((month-2)*30)+29
        print("Summary is:")
        print(Summary)
        print("leap year")
    elif year%4==0 and year%100==0 and year%400 !=0 :
        Summary= day + (month//2)+ ((month-2)*30)+28
        print("Summary is:")
        print(Summary)
    else:
        Summary= day + (month//2)+ ((month-2)*30)+28
        print("Summary is:")
        print(Summary)

print("Exercise 4 is done by Niloofar Amini")
